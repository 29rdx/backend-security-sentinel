import ipaddress
import urllib.parse

class SSRFScanner:
    """Validates destination URLs and IPs against SSRF threat vectors."""
    CLOUD_METADATA_IPS = {"169.254.169.254", "100.100.100.200", "fd00:ec2::254"}

    @classmethod
    def is_ssrf_vulnerable(cls, target_url: str) -> dict:
        parsed = urllib.parse.urlparse(target_url)
        hostname = parsed.hostname or ""
        try:
            ip = ipaddress.ip_address(hostname)
            is_private = ip.is_private or ip.is_loopback or ip.is_link_local
            is_cloud = str(ip) in cls.CLOUD_METADATA_IPS
        except ValueError:
            is_private = hostname.lower() in ("localhost", "127.0.0.1", "::1")
            is_cloud = False

        vulnerable = is_private or is_cloud
        return {
            "target_url": target_url,
            "vulnerable": vulnerable,
            "target_type": "cloud_metadata" if is_cloud else "private_network" if is_private else "public",
            "severity": "CRITICAL" if is_cloud else "HIGH" if is_private else "CLEAN"
        }
