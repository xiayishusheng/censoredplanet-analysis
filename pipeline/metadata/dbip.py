"""IP classificaation using the dbip database"""

import logging
import os
from typing import Optional, Tuple

import geoip2.database

from pipeline.metadata.mmdb_reader import mmdb_reader

DBIP_ISP = 'dbip-isp-2021-07-01.mmdb'


class DbipMetadata():
  """Lookup database for DBIP ASN and organization metadata."""

  def __init__(self, dbip_folder: str) -> None:
    """Create a DBIP Database.

      Args:
        dbip_folder: a folder containing a dbip file.
          Either a gcs filepath or a local system folder.
    """
    dbip_path = os.path.join(dbip_folder, DBIP_ISP)
    self.dbip_isp = mmdb_reader(dbip_path)

  def get_org(self, ip: str) -> Tuple[Optional[str], Optional[int]]:
    """Lookup the organization for an ip

    Args:
      ip: ip like 1.1.1.1

    Returns:
      Tuple of organization name and asn
    """
    try:
      ip_info = self.dbip_isp.enterprise(ip)
      return (ip_info.traits.organization,
              ip_info.traits.autonomous_system_number)

    except (ValueError, geoip2.errors.AddressNotFoundError) as e:
      logging.warning('DBIP: %s\n', e)
    return (None, None)


class FakeDbipMetadata():
  """A fake lookup table for testing DbipMetadata."""

  def __init__(self, _: str) -> None:
    super()

  # pylint: disable=no-self-use
  def get_org(self, _: str) -> Tuple[Optional[str], Optional[int]]:
    return ("Fake Cloudflare Sub-Org", 13335)
