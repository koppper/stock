import requests
import json

session = requests.Session()

session.headers.update({
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
})

cookies = {
    "stockx_device_id": "6738fe61-16bf-4aed-9cd4-2c916e48e5d5",
    "stockx_session_id": "bd0c13d7-8a07-4757-b247-86a23209bf51",
    "stockx_session": "0a3c0200-eb4f-4df4-bb24-a2bf7759d15d",
    "language_code": "en",
    "stockx_selected_region": "KZ",
    "display_location_selector": "false",
    "chakra-ui-color-mode": "dark",
    "is_gdpr": "false",
    "stockx_ip_region": "KZ",
    "pxcts": "65a5dd20-8c5f-11ef-a998-1f6c88a005e2",
    "_pxvid": "65a5ce14-8c5f-11ef-a996-9b4dbbddae21",
    "QuantumMetricSessionID": "76f1b5f5d77de55e5159f2ac5397dcef",
    "QuantumMetricUserID": "332afa2829cb0b465a759d48ec89e135",
    "rskxRunCookie": "0",
    "rCookie": "s6bob8o11ubktc7c0pza9m2d0v1dj",
    "ajs_anonymous_id": "bae6e570-bf52-4ef3-b7f5-5c99551e3cdc",
    "_gcl_au": "1.1.1302770080.1729152684",
    "rbuid": "rbos-e5db7a3f-06ea-46eb-b8ea-42408a45b0f1",
    "maId": "{\"pixlId\":45,\"cid\":\"8c9bd059b1c25216c42f73858e6b95b3\",\"sid\":\"b6c9a8bd-624c-4896-8a9f-24378ad8c897\",\"isSidSaved\":true,\"sessionStart\":\"2024-10-17T08:11:24.000Z\"}",
    "stockx_preferred_market_activity": "sales",
    "stockx_product_visits": "1",
    "stockx_homepage": "apparel",
    "cf_clearance": "bMyQqmR6c3Mv50RcKiHp8_Ap57Y91fSzP.LjaG3sjKM-1729153429-1.2.1.1-PbFh2dKvZdPXQKlmCfEDvzPYN7pKkgp78J.96FypZCQ2tGrplIxHrPtTu6cQFAyCnjNsmZAFWjPUGDM0_TGYrItF606D6SRBgDbc9k.CQ0S7VrUM_5vcQ7JhA5IAXe23T3uSphjmfAGu.9Jqf4vbmnA7vFnUnirbQlTqot.EgkxSR1D1BhT.eB5a8yXS45cZ8fxjiRaX3LkKYMef3pb0HXor5Z2ya_AEnY81bSRJ6qCmI_ERRmic1QZQfoZBl3.O1icEymHJZ7H4YjUOXejNFBtB7x1ODMlH1GmdtFHTOy81nb67BV_d1uBhhG6JKI.sDS0fs_8O8iX.5LNYwakOCTbGgdTrWfPZrLaDvLhJcCxnBTeQLolGy7g6rFPocSnG39xYGMqfkr_F.nLzRNOUOA",
    "__cf_bm": "Xc8GSqfUBwMV0F4bWjsLVGzLppdHEw22LzcxqVJr8sM-1729153673-1.0.1.1-DztOQJE0Mn._HgHCoDHuTrrLBWl8Yfi.dnDX3N41sByCNPmGs8X9sSaXYaxnfsdjXSBjXdb3n0iUjt3aU7jWwA",
    "_px3": "d9839a8e7167c3cd73ece1bab037c8189884eaae8d0667a995deaa3cda5b6ce7:4G+UOR87h4Em3zx8FOhiWHXH+XgwMHy7i43h9dNJOPuSHcCc33neeanE7XRQNxYmYSGDUVLloLZ8QnBk/7iCoQ==:1000:9yiN9cEn8GaTXktaYZmxwXbIuBBos31DlN7kTAWtvOVxDd0CwD+P5h621nXLKkrG0gKA6MY7RiGMAD0hqLrwsltQqIRLZTcZzFb2PCh4l2KFKrMUP9K14a0V0eKYiQ3i59MJ/ov+8RKONXMZdgYb0xCDoPtYYKciw80qKB7riKAG8LUEp/qCk0TYLKYHc5WR6GHKMC3u2UFbrC0ZTB+FfVF8Je76W/x6R+NB0VrvyZg=",
    "_tq_id.TV-5490813681-1.1a3e": "d6c337be9980bcc2.1729152685.0.1729153888..",
    "cto_bundle": "1E5sM19EZVExRWg2Ujk0V29YYkNCbkNsUkFGYTVBSFJrcGp1ZDI1UkowTHd3YUwwVFg5M3FOeDNKc3h6M25wJTJCRmhpJTJGTFdLN01CVmV4eDglMkZudDVUcEpOUkNhZHI2dkM0RzU1aURrZDRqOUdlZ0NwMjhPWEtmeVVCZ21ZaUF0TkhQeTBEc2NDb1liSGdJTnFzUEslMkZFbzg5YzROZyUzRCUzRA",
    "lastRskxRun": "1729153888685",
    "_uetsid": "667e01a08c5f11efbf0b59358c9da3bb|bzoyuy|2|fq3|0|1751",
    "_uetvid": "667e03f08c5f11ef93804fc4dbb996fd|16fvoc2|1729153888375|33|1|bat.bing.com/p/insights/c/t",
    "_dd_s": "rum=0&expire=1729154787430&logs=1&id=3e955aac-f43b-42fb-a0e4-8cfd99db5a46&created=1729152682099",
    "OptanonConsent": "isGpcEnabled=0&datestamp=Thu+Oct+17+2024+13%3A31%3A32+GMT%2B0500+(%D0%97%D0%B0%D0%BF%D0%B0%D0%B4%D0%BD%D1%8B%D0%B9+%D0%9A%D0%B0%D0%B7%D0%B0%D1%85%D1%81%D1%82%D0%B0%D0%BD)&version=202408.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=c200efa0-cbd0-4187-a967-3a05b8f75517&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1%2CC0005%3A1%2CC0003%3A1&AwaitingReconsent=false",
    "_pxde": "4116f2e8fe24e6dcd538561774323fa691d8bb521b3beb694b2a0a42d316cde8:eyJ0aW1lc3RhbXAiOjE3MjkxNTM4OTIyODYsImZfa2IiOjB9"
}


session.cookies.update(cookies)

headers = {
    "authority": "stockx.com",
    "accept": "application/json",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US",
    "apollographql-client-name": "Iron",
    "apollographql-client-version": "2024.10.13.00",
    "app-platform": "Iron",
    "app-version": "2024.10.13.00",
    "cache-control": "no-cache",
    "origin": "https://stockx.com",
    "pragma": "no-cache",
    "referer": "https://stockx.com/nike-dunk-low-diffused-taupe-womens",
    "sec-ch-prefers-color-scheme": "dark",
    "sec-ch-ua": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "selected-country": "KZ",
    "x-operation-name": "GetMarketData",
    "x-stockx-device-id": "6738fe61-16bf-4aed-9cd4-2c916e48e5d5",
    "x-stockx-session-id": "bd0c13d7-8a07-4757-b247-86a23209bf51",
    "Content-Type": "application/json",
}

# Тело запроса (payload)
payload = {
    "query": "query GetMarketData($id: String!, $currencyCode: CurrencyCode, $countryCode: String!, $marketName: String, $viewerContext: MarketViewerContext) {\n  product(id: $id) {\n    id\n    urlKey\n    listingType\n    title\n    uuid\n    contentGroup\n    sizeDescriptor\n    productCategory\n    lockBuying\n    lockSelling\n    media {\n      imageUrl\n    }\n    minimumBid(currencyCode: $currencyCode)\n    market(currencyCode: $currencyCode) {\n      state(country: $countryCode, market: $marketName) {\n        lowestAsk {\n          amount\n          chainId\n        }\n        highestBid {\n          amount\n        }\n        askServiceLevels {\n          expressExpedited {\n            count\n            lowest {\n              amount\n              chainId\n            }\n            delivery {\n              expectedDeliveryDate\n              latestDeliveryDate\n            }\n          }\n          expressStandard {\n            count\n            lowest {\n              amount\n            }\n            delivery {\n              expectedDeliveryDate\n              latestDeliveryDate\n            }\n          }\n        }\n        numberOfAsks\n        numberOfBids\n      }\n      salesInformation {\n        lastSale\n        salesLast72Hours\n      }\n      statistics(market: $marketName, viewerContext: $viewerContext) {\n        lastSale {\n          amount\n          changePercentage\n          changeValue\n          sameFees\n        }\n      }\n    }\n    variants {\n      id\n      market(currencyCode: $currencyCode) {\n        state(country: $countryCode, market: $marketName) {\n          lowestAsk {\n            amount\n            chainId\n          }\n          highestBid {\n            amount\n          }\n          askServiceLevels {\n            expressExpedited {\n              count\n              lowest {\n                amount\n                chainId\n              }\n              delivery {\n                expectedDeliveryDate\n                latestDeliveryDate\n              }\n            }\n            expressStandard {\n              count\n              lowest {\n                amount\n              }\n              delivery {\n                expectedDeliveryDate\n                latestDeliveryDate\n              }\n            }\n          }\n          numberOfAsks\n          numberOfBids\n        }\n        salesInformation {\n          lastSale\n          salesLast72Hours\n        }\n        statistics(market: $marketName, viewerContext: $viewerContext) {\n          lastSale {\n            amount\n            changePercentage\n            changeValue\n            sameFees\n          }\n        }\n      }\n    }\n  }\n}",
    "variables": {
        "id": "nike-dunk-low-diffused-taupe-womens",
        "currencyCode": "USD",
        "countryCode": "KZ",
        "marketName": "KZ",
        "viewerContext": "BUYER"
    },
    "operationName": "GetMarketData"
}

url = "https://stockx.com/api/p/e"

response = session.post(url, headers=headers, json=payload)
response_data = response.json()
def parse_product_data(data):
    product = data['data']['product']
    title = product.get('title', 'N/A')
    url = product.get('urlKey', 'N/A')
    image_url = product['media'].get('imageUrl', 'N/A')
    
    variants = []
    for variant in product['variants']:
        lowest_ask = variant['market']['state']['lowestAsk'].get('amount') if variant['market']['state'].get('lowestAsk') else None
        highest_bid = variant['market']['state']['highestBid'].get('amount') if variant['market']['state'].get('highestBid') else None
        # image_url = variant['media'].get('imageUrl') if variant['media'].get('imageUrl') else None

        variant_info = {
            'title': title,
            'variant_id': variant['id'],
            'lowest_ask': lowest_ask,
            'highest_bid': highest_bid,
            "image_url": image_url
        }
        variants.append(variant_info)
    
    parsed_data = {
        'title': title,
        'product_url': f"https://stockx.com/{url}",
        'image_url': image_url,
        'variants': variants
    }
    return parsed_data

parsed_data = parse_product_data(response_data)
print(json.dumps(parsed_data, indent=4))
result = json.dumps(parsed_data, indent=4)
if response.status_code == 200:
    with open("market_data.json", "w", encoding="utf-8") as f:
        json.dump(parsed_data, f, ensure_ascii=False, indent=4)
    print("Данные успешно сохранены в файл 'market_data.json'")
else:
    print(f"Ошибка при запросе: {response.status_code}")
    print(f"Текст ошибки: {response.text}")

