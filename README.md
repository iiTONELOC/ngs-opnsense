# NGS OPNSense API

A Python Module for interacting with the OPNSense API

Uses [requests](https://requests.readthedocs.io/en/latest/), [urllib3](https://github.com/urllib3/urllib3), and [pydantic](https://docs.pydantic.dev/latest/)

## Table of Contents

- [Usage](#usage)
- [OPNSense API Structure](#opnsense-api-structure)
- [License](#license)

## Usage

```python
import json
from NG_OPNSense import OPNSenseAPI

# Create an instance of the OPNSense API
opnsense = OPNSenseAPI(
    url="https://opnsense.local",
    apiKey="myApiKey",
    apiSecret="myApiSecret")

# To interact with the OPNSense API, use the same methods provided by
# the OPNSense API: https://docs.opnsense.org/development/api.html

# For example, to fetch aliases:
aliases =  opnsense.coreAPI.firewall.alias.get()

# Print the aliases
print(json.dumps(aliases, indent=4))
```

## OPNSense API Structure

`This is a work in progress and not all endpoints have/will be implemented`

The tree below
presents a high-level overview of the [OPNSense API](https://docs.opnsense.org/development/api.html).

Portions that are linked, link to documentation for their implementation.

OPNsense API  
│  
├── [`Core API`](./docs/core.md)  
│   ├── /api/captiveportal  
│   ├── /api/core  
│   ├── /api/cron  
│   ├── /api/dhcp  
│   ├── /api/dhcpv4  
│   ├── /api/dhcpv6  
│   ├── /api/dhcrelay  
│   ├── /api/diagnostics  
│   ├── [`/api/firewall`](./docs/core/firewall.md)  
│   ├── /api/firmware  
│   ├── /api/ids  
│   ├── /api/interfaces  
│   ├── /api/ipsec  
│   ├── /api/kea  
│   ├── /api/menu  
│   ├── /api/monit  
│   ├── /api/openvpn  
│   ├── /api/proxy  
│   ├── /api/routes  
│   ├── /api/routing  
│   ├── /api/syslog  
│   ├── /api/trafficshaper  
│   ├── /api/trust  
│   ├── /api/unbound  
│   └── /api/wireguard  
│  
├── Plugins API  
│   ├── /api/acmeclient  
│   ├── /api/apcupsd  
│   ├── /api/backup  
│   ├── /api/bind  
│   ├── /api/caddy  
│   ├── /api/chrony  
│   ├── /api/cicap  
│   ├── /api/clamav  
│   ├── /api/collectd  
│   ├── /api/crowdsec  
│   ├── /api/dechw  
│   ├── /api/diagnostics  
│   ├── /api/dnscryptproxy  
│   ├── /api/dyndns  
│   ├── /api/fetchmail  
│   ├── /api/forms  
│   ├── /api/freeradius  
│   ├── /api/ftpproxy  
│   ├── /api/gridexample  
│   ├── /api/haproxy  
│   ├── /api/helloworld  
│   ├── /api/hwprobe  
│   ├── /api/iperf  
│   ├── /api/lldpd  
│   ├── /api/maltrail  
│   ├── /api/mdnsrepeater  
│   ├── /api/muninnode  
│   ├── /api/ndproxy  
│   ├── /api/netdata  
│   ├── /api/netsnmp  
│   ├── /api/nginx  
│   ├── /api/nodeexporter  
│   ├── /api/nrpe  
│   ├── /api/ntopng  
│   ├── /api/nut  
│   ├── /api/openconnect  
│   ├── /api/postfix  
│   ├── /api/proxy  
│   ├── /api/proxysso  
│   ├── /api/proxyuseracl  
│   ├── /api/puppetagent  
│   ├── /api/qemuguestagent  
│   ├── /api/quagga  
│   ├── /api/radsecproxy  
│   ├── /api/redis  
│   ├── /api/relayd  
│   ├── /api/rspamd  
│   ├── /api/shadowsocks  
│   ├── /api/siproxd  
│   ├── /api/smart  
│   ├── /api/softether  
│   ├── /api/sslh  
│   ├── /api/stunnel  
│   ├── /api/tayga  
│   ├── /api/telegraf  
│   ├── /api/tftp  
│   ├── /api/tinc  
│   ├── /api/tor  
│   ├── /api/udpbroadcastrelay  
│   ├── /api/vnstat  
│   ├── /api/wazuhagent  
│   ├── /api/wireguard  
│   ├── /api/wol  
│   ├── /api/zabbixagent  
│   ├── /api/zabbixproxy  
│   └── /api/zerotier  
│
└── Business Edition API
    └── /api/opnbe  

## Contributing

This project is welcome to contributions. As mentioned above, their API is quite extensive and it is only practical for me to implement endpoints that I require, or think I may require.

To help out please feel free to fork the repository and submit a pull request.

## License

[License](./LICENSE)
