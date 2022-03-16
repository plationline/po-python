import base64
import binascii
from Cryptodome.Cipher import AES, PKCS1_v1_5
from Crypto.PublicKey import RSA
import random
import string
from Crypto.Util.Padding import pad, unpad

chars = string.ascii_lowercase + string.digits
__key__ = ''.join(random.choice(chars) for i in range(32)).encode()

#from merchants account
__public_key__ = """-----BEGIN PUBLIC KEY-----

-----END PUBLIC KEY-----"""

#from merchants account
__iv__ = '0000000000000000'

def encrypt(raw):
    raw = pad(raw.encode(), 16)
    iv = __iv__.encode()

    cipher = AES.new(key= __key__, mode=AES.MODE_CBC, iv=iv)
    return binascii.hexlify(base64.b64encode(cipher.encrypt(raw))).decode()

def rsa_encrypt(text):
    rsa_public_key = RSA.importKey(__public_key__)
    rsa_public_key = PKCS1_v1_5.new(rsa_public_key)
    encrypted_text = rsa_public_key.encrypt(text)
    return base64.b64encode(encrypted_text).decode()

print("AES")
print(encrypt("<po_auth_request><f_website>demo.ro</f_website><f_test_request>1</f_test_request><f_sequence>970</f_sequence><f_login>DEMO demo.ro</f_login><f_timestamp>2022-03-15T10:41:20</f_timestamp><f_action>2</f_action><f_order_number>SO002</f_order_number><f_amount>10.2</f_amount><f_currency>RON</f_currency><f_auth_minutes>20</f_auth_minutes><f_language>RO</f_language><customer_info><contact><f_email>email@dom.com</f_email><f_phone>0720000000</f_phone><f_mobile_number>0720000000</f_mobile_number><f_send_sms>1</f_send_sms><f_first_name>Test</f_first_name><f_last_name>PO</f_last_name></contact><invoice><f_company>company</f_company><f_cui /><f_reg_com /><f_cnp /><f_zip /><f_country>Romania</f_country><f_state>Bucuresti</f_state><f_city>Bucuresti</f_city><f_address>Address</f_address></invoice></customer_info><shipping_info><same_info_as>0</same_info_as><contact><f_email>email@dom.com</f_email><f_phone>0720000000</f_phone><f_mobile_number>0720000000</f_mobile_number><f_send_sms>1</f_send_sms><f_first_name>Test</f_first_name><f_last_name>Po</f_last_name></contact><address><f_company>company</f_company><f_zip /><f_country>Romania</f_country><f_state>Bucuresti</f_state><f_city>Bucuresti</f_city><f_address>Address</f_address></address></shipping_info><transaction_relay_response><f_relay_response_url>https://domain.com/auth_response.py</f_relay_response_url><f_relay_method>PTOR</f_relay_method><f_post_declined>1</f_post_declined><f_relay_handshake>1</f_relay_handshake></transaction_relay_response><f_order_string>Order number SO0002 on website http://domain.com</f_order_string><f_order_cart><item><prodid>1</prodid><name>Produs 1</name><description>description 1</description><qty>2</qty><itemprice>11.05</itemprice><vat>2.22</vat><stamp>2022-03-15</stamp><prodtype_id>0</prodtype_id></item></f_order_cart><f_customer_ip>127.0.0.1</f_customer_ip></po_auth_request>"))
print("RSA")
print(rsa_encrypt(__key__))

# this is an encryption example, the validation against schema and the SOAP call to Plati.Online must be implemented by yourself
#you must generate po_auth_request XML based on your website order info, validate it against schema and send it via SOAP request to Plati.Online. You will obtain a redirect URL where your customer can pay
