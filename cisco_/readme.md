
In r1
- `conf t`    
- `license boot module c1900 technology-package securityk9` (do this in both routers)
- `copy run start` (to save the config)
- `reload`
- `en` -> `show version` ( to confirm success )


STEP 1> ACL
In r1 config
- `access-list 100 permit ip 192.168.1.0 0.0.0.255 192.168.3.0 0.0.0.255`
In r3 config
- `access-list 100 permit ip 192.168.3.0 0.0.0.255 192.168.1.0 0.0.0.255`


STEP 2>ISAKMP
paste on both router r1 r3
crypto isakmp policy 10
encryption aes 256
authentication pre-share
group 5

(group 5 - diffie hellman )
- `crypto isakmp key secretkey address 209.165.200.1` (on r1)
- `crypto isakmp key secretkey address 209.165.100.1` (on r3)

STEP 3>IPsec tranform set
- `crypto ipsec transform-set R1-R3 esp-aes 256 esp-sha-hmac`
- `crypto ipsec transform-set R3-R1 esp-aes 256 esp-sha-hmac`

STEP4> set up crypto map
 - for r1
crypto map IPSEC-MAP 10 ipsec-isakmp 
 set peer 209.165.200.1
 set pfs group5
 set security-association lifetime seconds 86400
 set transform-set R1-R3 
 match address 100

 - for r3
crypto map IPSEC-MAP 10 ipsec-isakmp 
 set peer 209.165.100.1
 set pfs group5
 set security-association lifetime seconds 86400
 set transform-set R3-R1 
 match address 100


# turn on the crypto map
 - conf t
 - int g0/0
 - crypto map IPSEC-MAP

 