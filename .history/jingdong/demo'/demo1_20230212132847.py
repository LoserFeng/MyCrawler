
import requests

headers={


    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "max-age=0",
    "sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Microsoft Edge\";v=\"110\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "cookie": "shshshfpa=a59ef60d-c8a6-92ba-2baf-a646895cc98d-1672212324; shshshfpb=yZaSjZXfeZ-R-j6eY1Nun6A; __jdu=16722123231461165655386; areaId=15; PCSYCityID=CN_330000_330100_0; ipLoc-djd=15-1213-3038-59931; jwotest_product=99; pinId=F0lqqKsS7Ce1ffsfn98I-w; pin=LOSER%E4%B8%B0; unick=LOSER%E4%B8%B0; _tp=Iz8Q38tsk7Xe1Xc1Cy0l4Q%3D%3D; _pst=LOSER%E4%B8%B0; unpl=JF8EAKhnNSttXE5dURkLHxYVQwhVW11bHkdQPTUHAQ0NTwNXTgYeQUB7XlVdXxRKFB9vZBRUX1NLUA4fAysSEHtdVV9fCU0eAGhgNWRYW0xTBCsBGyIRe11TWF4LSxQBbGUFUVpYS1MBHAYfEBlMbVVuXQBMJwRvZgJVX1h7ZAQrAysTIB0zVF9cCUofBWxkBhldX01XBhsBGRESS1hTXl0PTxAHa2UMU21Ze1c; __jdv=122270672|kong|t_1003078266_|jingfen|548e385549d041bdabcc3dad5fcd54ba|1676178951001; JSESSIONID=026E85395007B5B211EB44E11E585C92.s1; TrackID=153eT-bS7-TH0zTiURvbcsXJ906H2je9nODkD5QrvdAOSH3lh5WOMlE_E_WvGLCO6VwC1LDNjV1QzURU_Em52NPCWhCOon3yKMb1h5OHxvK_zNdqe0N90kh5n5LHhz2Na; thor=B0FCAB6E82CA81C65C8CD0C89AFF0FD42C09EC761E24C53E3B9B787FDEA9C34F252E2965DB3C8B512E134B2A3D7D87DA634245864EC287BD50329BAC3B0465B17CED742DCF722924F74ABECF44140EAEF8BF76027B79F1E3F60156641A50A21450321A78F216354AA0C8621E6134873F1B2ADC1F1DFD37424582D907C2BBDCA8; ceshi3.com=000; __jda=76161171.16722123231461165655386.1672212323.1676178924.1676178951.16; __jdb=76161171.8.16722123231461165655386|16.1676178951; __jdc=76161171; shshshfp=bc1f4aeb46f0dda1cb207282332d7d4a; shshshfpx=a59ef60d-c8a6-92ba-2baf-a646895cc98d-1672212324; shshshsID=644c61c7f485dcd2b6d7bdff14f3eb4f_9_1676179298399; 3AB9D23F7A4B3C9B=FTSDKAYZNZKCZEI2SHBQY2UVW7R5ZBD7C4KZOV6I52DX4YPOAOJ2OLORCGQB5P35WXNCTLBOXG6CZWIZCSDSGUAJ5U; joyya=0.1676179528.22.0z6dzx5"
}



url=f'https://search.jd.com/Search?keyword=%E7%BD%91%E7%BB%9C%E6%9C%BA%E9%A1%B6%E7%9B%92&enc=utf-8&spm=a.0.0'
res=requests.get(url=url,headers=headers)


print(res.text)