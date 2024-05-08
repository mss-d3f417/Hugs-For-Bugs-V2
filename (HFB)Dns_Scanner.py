# Made By D3F417 - With Purple Heart
# Kidi Don't Copy This Code ! 
# GitHub : https://github.com/mss-d3f417
# Site : https://d3f417.info

import dns.resolver

def dns_lookup(target_domain):
    record_types = ["A", "AAAA", "CNAME", "MX", "NS", "SOA", "TXT"]
    resolver = dns.resolver.Resolver()
    for record_type in record_types:
        try:
            answers = resolver.resolve(target_domain, record_type)
        except dns.resolver.NoAnswer:
            continue
        print(f"{record_type} records for {target_domain}:")
        for rdata in answers:
            print(f" {rdata}")

if __name__ == "__main__":
    target_domain = input("HFB > Domaini Ke Mikhay Dns Hasho Ro Bede KIRI: ")
    dns_lookup(target_domain)