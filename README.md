# Request Assias 

The request that goes on assias 


## Home 

### Request

```bash
curl --compressed 'https://api.assai8.com/api/public/home?d=1736647103588&language_type=en' \
-X 'GET' \
-H 'Accept: application/json, text/plain, */*' \
-H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuYXNzYWk4LmNvbSIsImF1ZCI6ImFwaS5hc3NhaTguY29tIiwiaWF0IjoxNzM2NjQ3MTAzLCJuYmYiOjE3MzY2NDcxMDMsImV4cCI6MTczNzUxMTEwMywianRpIjp7ImlkIjoyMjI5OSwidHlwZSI6ImFwaSJ9fQ.ehsnnLlohHZU0F_7FYUtCJGhRi1xfUjg1xcY3_BYTks' \
-H 'Origin: https://assai8.com' \
-H 'Referer: https://assai8.com/' \
-H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Safari/605.1.15' \
-H 'Accept-Encoding: gzip, deflate, br' \
-H 'Accept-Language: en-US' \
-H 'Cookie: cf_clearance=UgYJNbIj4aedMxUUgRD05rAuh8x4OCzhk1FAXe9kVj0-1736647020-1.2.1.1-_doefsuEm.iryIB07VugSWoMjWEOc7e9DeQ1vp84M.jdZ9jWSM_q0KLIUHGiAbA6hwun1RdSxDJkyEmV5XAwvTy2OcELo_npWudWBRQHrGIrxB.aV5AXq2Leaw3Euth2p3ZxxiTrY85ecMk5Qe3uTEHHMNegsOD2ilAs5XNJli9cUX7_ILR7VJSnaQygybyCGXyMkZ5w7bvthCFWU2BIgiy8Dxy_A1pNqzcf1jx3YPHjmBlwa3ynyftzVW34Cbp.wq24gZjCxJyBVhW.U6s8Zg0yjqlUPAZleBT3Qfze94c' \
-H 'Sec-Fetch-Dest: empty' \
-H 'Sec-Fetch-Mode: cors' \
-H 'Sec-Fetch-Site: same-site' \
-H 'st-lang: en' \
-H 'st-ctime: 1736647103588' \
-H 'st-ttgn: 3977480070d10eb04d7956eec4799632'
``` 

### Response

```json
 {
    "status": 200,
    "data": {
        "index": {
            "user": {
                "account": "6617186900",
                "base_money": "32.200000",
                "brokerage_money": "0.000000",
                "experience_money": "0.000000",
                "financial_money": "0.000000",
                "recharge_account": "0.000000",
                "recharge_money": 0,
                "withdrawal_money": 0,
                "invitation_code": "941870",
                "language": "en",
                "level": 0,
                "add_time": 1736444818,
                "sign_in_day": 0,
                "sign_last_time": 0,
                "avatar": "https://t.me/i/userpic/320/7et6AQv4O8-uPEYSN0ckeLCDcABy69tki4zqHvF8uwsVvKYWSl8hGs3A72njso6o.svg",
                "total_invest_income": "0.000000",
                "total_task_income": "32.200000",
                "mining_start_time": 1736634008,
                "mining_end_time": 1736648408,
                "mining_speed": 4.025,
                "user_mining_time": 4,
                "tg_show_name": "somto ",
                "one_spread_uid": 17293,
                "level_name": "VIP 0",
                "mining": "4.025000",
                "mining_time": 4,
                "invite_user": "64842****",
                "total_money": 32.2,
                "total_income": 32.2,
                "airdrop_mining_status": 1
            },
            "new_message_count": 0,
            "new_pop_message_count": 0
        },
        "task_reset_time": "13:00",
        "rebate_time": 50496,
        "system": {
            "index_video_url": "https://api.assai8.com/upload/files/66d85db54861.mp4",
            "index_video_is_show": "false",
            "is_show_fake_data": "false",
            "index_user_num": "68552",
            "index_profit_num": "231144266",
            "transfer_is_pwd": "true",
            "partner_is_show": "true",
            "supervision_is_show": "true",
            "can_transfer_friend": "false",
            "can_transfer_invest_friend": "false",
            "is_enable_sign": "false",
            "white_paper": "https://tron.network/static/doc/white_paper_v_2_0.pdf",
            "is_experience": "false",
            "experience_unlock_type": "2"
        },
        "slide": [],
        "level_info": {
            "level": "VIP 0",
            "recharge_money": 0,
            "level_info": [
                {
                    "id": 24,
                    "name": "VIP 0",
                    "recharge_min": "0.000000",
                    "recharge_max": "0.000000",
                    "grade": 0,
                    "mining": "4.025000",
                    "invitation_rebate": "",
                    "recharge_rebate": "[8,3,2,1,1]",
                    "mining_rebate": "",
                    "finance_rebate": "",
                    "again_charge_percent": "0.00",
                    "again_charge_cap": "0.00",
                    "add_time": 1727791313,
                    "is_show": 1,
                    "is_del": 0,
                    "image": "https://api.assai8.com/upload/img/677cefc6d4f9.webp",
                    "withdraw_trx_min_money": "[0,0,0]",
                    "withdraw_usdt_min_money": "[0,0,0]",
                    "daily_brokerage_transfer_limit": "0.00",
                    "month_brokerage_transfer_limit": "0.00",
                    "is_extract": 1,
                    "daily_invest_transfer_limit": "0.00",
                    "month_invest_transfer_limit": "0.00",
                    "extract_week": "1,2,3,4,5,6,7",
                    "mining_time": 4
                },
                {
                    "id": 13,
                    "name": "VIP1",
                    "recharge_min": "120.000000",
                    "recharge_max": "100.000000",
                    "grade": 1,
                    "mining": "4.250000",
                    "invitation_rebate": "",
                    "recharge_rebate": "[8,3,2,1,1]",
                    "mining_rebate": "[1,2,3]",
                    "finance_rebate": "[1,2,3]",
                    "again_charge_percent": "0.00",
                    "again_charge_cap": "0.00",
                    "add_time": 1725875248,
                    "is_show": 1,
                    "is_del": 0,
                    "image": "https://api.assai8.com/upload/img/677cf01896b5.webp",
                    "withdraw_trx_min_money": "[0,0,0]",
                    "withdraw_usdt_min_money": "[0,0,0]",
                    "daily_brokerage_transfer_limit": "0.00",
                    "month_brokerage_transfer_limit": "0.00",
                    "is_extract": 1,
                    "daily_invest_transfer_limit": "0.00",
                    "month_invest_transfer_limit": "0.00",
                    "extract_week": "1,2,3,4,5,6,7",
                    "mining_time": 24
                },
                {
                    "id": 14,
                    "name": "VIP2 ",
                    "recharge_min": "500.000000",
                    "recharge_max": "100.000000",
                    "grade": 2,
                    "mining": "5.800000",
                    "invitation_rebate": "",
                    "recharge_rebate": "[8,3,2,1,1]",
                    "mining_rebate": "[1,2,3]",
                    "finance_rebate": "[1,2,3]",
                    "again_charge_percent": "0.00",
                    "again_charge_cap": "0.00",
                    "add_time": 1725875310,
                    "is_show": 1,
                    "is_del": 0,
                    "image": "https://api.assai8.com/upload/img/677cf02ba129.webp",
                    "withdraw_trx_min_money": "[0,0,0]",
                    "withdraw_usdt_min_money": "[0,0,0]",
                    "daily_brokerage_transfer_limit": "1000.00",
                    "month_brokerage_transfer_limit": "30000.00",
                    "is_extract": 1,
                    "daily_invest_transfer_limit": "10000.00",
                    "month_invest_transfer_limit": "10000.00",
                    "extract_week": "1,2,3,4,5,6,7",
                    "mining_time": 24
                },
                {
                    "id": 16,
                    "name": "VIP3",
                    "recharge_min": "5000.000000",
                    "recharge_max": "0.000000",
                    "grade": 3,
                    "mining": "9.800000",
                    "invitation_rebate": "",
                    "recharge_rebate": "[8,3,2,1,1]",
                    "mining_rebate": "",
                    "finance_rebate": "",
                    "again_charge_percent": "0.00",
                    "again_charge_cap": "0.00",
                    "add_time": 1726709344,
                    "is_show": 1,
                    "is_del": 0,
                    "image": "https://api.assai8.com/upload/img/677cf03a457b.webp",
                    "withdraw_trx_min_money": "[0,0,0]",
                    "withdraw_usdt_min_money": "[0,0,0]",
                    "daily_brokerage_transfer_limit": "0.00",
                    "month_brokerage_transfer_limit": "0.00",
                    "is_extract": 1,
                    "daily_invest_transfer_limit": "0.00",
                    "month_invest_transfer_limit": "0.00",
                    "extract_week": "1,2,3,4,5,6,7",
                    "mining_time": 24
                },
                {
                    "id": 26,
                    "name": "VIP4",
                    "recharge_min": "10000.000000",
                    "recharge_max": "0.000000",
                    "grade": 4,
                    "mining": "13.000000",
                    "invitation_rebate": "",
                    "recharge_rebate": "[8,3,2,1,1]",
                    "mining_rebate": "",
                    "finance_rebate": "",
                    "again_charge_percent": "0.00",
                    "again_charge_cap": "0.00",
                    "add_time": 1736235214,
                    "is_show": 1,
                    "is_del": 0,
                    "image": "https://api.assai8.com/upload/img/677cf049c3ae.webp",
                    "withdraw_trx_min_money": "[0,0,0]",
                    "withdraw_usdt_min_money": "[0,0,0]",
                    "daily_brokerage_transfer_limit": "0.00",
                    "month_brokerage_transfer_limit": "0.00",
                    "is_extract": 1,
                    "daily_invest_transfer_limit": "0.00",
                    "month_invest_transfer_limit": "0.00",
                    "extract_week": "1,2,3,4,5,6,7",
                    "mining_time": 24
                },
                {
                    "id": 27,
                    "name": "VIP5",
                    "recharge_min": "50000.000000",
                    "recharge_max": "0.000000",
                    "grade": 5,
                    "mining": "20.000000",
                    "invitation_rebate": "",
                    "recharge_rebate": "[8,3,2,1,1]",
                    "mining_rebate": "",
                    "finance_rebate": "",
                    "again_charge_percent": "0.00",
                    "again_charge_cap": "0.00",
                    "add_time": 1736235313,
                    "is_show": 1,
                    "is_del": 0,
                    "image": "https://api.assai8.com/upload/img/677cf0563fb3.webp",
                    "withdraw_trx_min_money": "[0,0,0]",
                    "withdraw_usdt_min_money": "[0,0,0]",
                    "daily_brokerage_transfer_limit": "0.00",
                    "month_brokerage_transfer_limit": "0.00",
                    "is_extract": 1,
                    "daily_invest_transfer_limit": "0.00",
                    "month_invest_transfer_limit": "0.00",
                    "extract_week": "1,2,3,4,5,6,7",
                    "mining_time": 24
                },
                {
                    "id": 28,
                    "name": "VIP6",
                    "recharge_min": "100000.000000",
                    "recharge_max": "0.000000",
                    "grade": 6,
                    "mining": "30.000000",
                    "invitation_rebate": "",
                    "recharge_rebate": "[8,3,2,1,1]",
                    "mining_rebate": "",
                    "finance_rebate": "",
                    "again_charge_percent": "0.00",
                    "again_charge_cap": "0.00",
                    "add_time": 1736235434,
                    "is_show": 1,
                    "is_del": 0,
                    "image": "https://api.assai8.com/upload/img/677cf066f036.webp",
                    "withdraw_trx_min_money": "[0,0,0]",
                    "withdraw_usdt_min_money": "[0,0,0]",
                    "daily_brokerage_transfer_limit": "0.00",
                    "month_brokerage_transfer_limit": "0.00",
                    "is_extract": 1,
                    "daily_invest_transfer_limit": "0.00",
                    "month_invest_transfer_limit": "0.00",
                    "extract_week": "1,2,3,4,5,6,7",
                    "mining_time": 24
                },
                {
                    "id": 29,
                    "name": "VIP7",
                    "recharge_min": "500000.000000",
                    "recharge_max": "0.000000",
                    "grade": 7,
                    "mining": "50.000000",
                    "invitation_rebate": "",
                    "recharge_rebate": "[8,3,2,1,1]",
                    "mining_rebate": "",
                    "finance_rebate": "",
                    "again_charge_percent": "0.00",
                    "again_charge_cap": "0.00",
                    "add_time": 1736235480,
                    "is_show": 1,
                    "is_del": 0,
                    "image": "https://api.assai8.com/upload/img/677cf071549e.webp",
                    "withdraw_trx_min_money": "[0,0,0]",
                    "withdraw_usdt_min_money": "[0,0,0]",
                    "daily_brokerage_transfer_limit": "0.00",
                    "month_brokerage_transfer_limit": "0.00",
                    "is_extract": 1,
                    "daily_invest_transfer_limit": "0.00",
                    "month_invest_transfer_limit": "0.00",
                    "extract_week": "1,2,3,4,5,6,7",
                    "mining_time": 24
                }
            ]
        },
        "notice": [
            {
                "id": 661,
                "update_time": 1736249654,
                "language_type": "en",
                "remark": "英语",
                "content": "<p>Welcome to our community! 🎉You have taken the first step to obtain free tokens, and there will be more exciting rewards waiting for you in the future! </p><p>▲●▲Join the link via Telegram: <a href=\"https://t.me/ASSAI8Bot?start=ref_470179\" target=\"_blank\" rel=\"noopener\">https://t.me/ASSAI8Bot ?start=ref_470179</a></p><p>Official customer service: <a href=\"https://t.me/wwwassai8com\" target=\"_blank\" rel=\"noopener\">https://t.me/wwwassai8com</a></p><p>Official group: <a href=\"https://t.me/Assai8com\" target=\"_blank\" rel=\"noopener\">https://t.me/Assai8com</a></p><p>1. Users can purchase mining tool accelerator cards on the website by recharging USDT to accelerate the daily mining of ASSAI tokens, thereby digging out more ASSAI tokens and obtaining mining income every day. </p><p>2. Users can exchange the ASSAI tokens mined by the ASSAI platform into USDT and withdraw them to their wallets. </p><p>3. Invite customers to deposit 15USDT and have a chance to win 1,00-1,000,00 ASSAI coins</p>",
                "add_time": 0,
                "status": 1,
                "sort": 0,
                "template": "",
                "template_id": 49,
                "title": "Latest News"
            },
            {
                "id": 683,
                "update_time": 1736236623,
                "language_type": "en",
                "remark": "英语",
                "content": "<p>ASSAI coin exchange rate: 1000 ASSAI coins can be exchanged for 2 USDT.</p><p> </p><p>ASSAI minimum deposit: 15 USDT, minimum withdrawal: 2 USDT!</p><p> </p><p>Minimum withdrawal amount 2USDT-99999USDT!</p><p> </p><p>Withdrawal is extremely fast in 1-3 minutes, 24/7 withdrawal, no holidays!</p><p> </p><p>In order to facilitate users from different countries to deposit and withdraw, the platform uses BEP20-USDT and TRC20-USDT as the only withdrawal currency!</p><p> </p><p>You can use USDT to purchase the following packages to increase mining computing power and obtain more ASSAI coin computing power.</p><p> </p><p> </p><p>15USDT to purchase mining tool level 1, 24-hour mining income 1000 ASSAI coins, value = 2USDT</p><p> </p><p>80USDT to purchase mining tool level 2, 24-hour mining income 5400 ASSAI coins, value = 10.8USDT</p><p> </p><p>280USDT to purchase mining tool level 3, 24-hour mining income 19750 ASSAI coins, value = 39.5USDT</p><p> </p><p>980USDT to purchase mining tool level 4, 24-hour mining income 71250 ASSAI coins, value = 142.5USDT</p><p> </p><p>2800USDT to purchase mining tool level 5, 24-hour mining income 209250 ASSAI Coin, value = 418.5USDT</p><p> </p><p>5800USDT to purchase mining tool level 6, 24H mining income 446250 ASSAI coins, value = 892.5USDT</p><p> </p><p>18000USDT to purchase mining tool level 7, 24H mining income 1429000 ASSAI coins, value = 2858USDT</p><p> </p><p>58000USDT to purchase mining tool level 8, 24H mining income 4833000 ASSAI coins, value = 9666USDT</p><p> </p><p>100000USDT to purchase mining tool level 9, 24H mining income 8925000 ASSAI coins, value = 17850USDT</p><p> </p><p>---------------------------</p><p>●: Invitation Rewards</p><p> </p><p>Invite new customers to join the deposit purchase tool to get high 5-level rebates (15%)</p><p> </p><p>Level 1 gets 8%. For example, if the team deposits 100USDT, it can get 8USDT</p><p> </p><p>Level 2 gets 3%. For example, if the team deposits 100USDT, it can get 3USDT</p><p> </p><p>Level 3 gets 2%. For example, if the team deposits 100USDT, it can get 2USDT</p><p> </p><p>Level 4 gets 1%. For example, if the team deposits 100USDT, it can get 1USDT</p><p> </p><p>Level 5 gets 1%. For example, if the team deposits 100USDT, it can get 1USDT</p><p> </p><p> </p><p>Currency ranking rewards are issued every 7 days:</p><p> </p><p>1st-5th place: 50,00ASSAI coins</p><p> </p><p>6th-10th place: 30,00ASSAI coins</p><p> </p><p>11th-20th place: 20,00ASSAI coins</p><p> </p><p>21st-50th place: 10,00ASSAI coins</p><p> </p><p> </p><p>Team invitation ranking rewards are issued every 7 days:</p><p> </p><p>1st-5th place: 50,00ASSAI coins</p><p> </p><p>6th-10th place: 30,00ASSAI coins</p><p> </p><p>11th-20th place: 20,00ASSAI coins</p><p> </p><p>21st-100th place: 10,00ASSAI coins</p><p> </p><p>You can promote our platform through referral links, or tell your friends on Facebook, Twitter, Instagram, YouTube, TikTok, KAOKAO, WhatsApp, Telegram, and you can earn up to 15% rewards when someone registers or tops up.</p>",
                "add_time": 0,
                "status": 1,
                "sort": 1,
                "template": "",
                "template_id": 50,
                "title": "Latest News 1"
            }
        ]
    },
    "msg": "ok"
}
```

## Mine

### Request 

```bash
curl --compressed 'https://api.assai8.com/api/user/mine' \
-X 'GET' \
-H 'Accept: application/json, text/plain, */*' \
-H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuYXNzYWk4LmNvbSIsImF1ZCI6ImFwaS5hc3NhaTguY29tIiwiaWF0IjoxNzM2NjQ3MTAzLCJuYmYiOjE3MzY2NDcxMDMsImV4cCI6MTczNzUxMTEwMywianRpIjp7ImlkIjoyMjI5OSwidHlwZSI6ImFwaSJ9fQ.ehsnnLlohHZU0F_7FYUtCJGhRi1xfUjg1xcY3_BYTks' \
-H 'Origin: https://assai8.com' \
-H 'Referer: https://assai8.com/' \
-H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Safari/605.1.15' \
-H 'Accept-Encoding: gzip, deflate, br' \
-H 'Accept-Language: en-US' \
-H 'Cookie: cf_clearance=UgYJNbIj4aedMxUUgRD05rAuh8x4OCzhk1FAXe9kVj0-1736647020-1.2.1.1-_doefsuEm.iryIB07VugSWoMjWEOc7e9DeQ1vp84M.jdZ9jWSM_q0KLIUHGiAbA6hwun1RdSxDJkyEmV5XAwvTy2OcELo_npWudWBRQHrGIrxB.aV5AXq2Leaw3Euth2p3ZxxiTrY85ecMk5Qe3uTEHHMNegsOD2ilAs5XNJli9cUX7_ILR7VJSnaQygybyCGXyMkZ5w7bvthCFWU2BIgiy8Dxy_A1pNqzcf1jx3YPHjmBlwa3ynyftzVW34Cbp.wq24gZjCxJyBVhW.U6s8Zg0yjqlUPAZleBT3Qfze94c' \
-H 'Sec-Fetch-Dest: empty' \
-H 'Sec-Fetch-Mode: cors' \
-H 'Sec-Fetch-Site: same-site' \
-H 'st-lang: en' \
-H 'st-ttgn: d9ac52466794fd405617002e92c425f9'
```

### Response 

```json
{
    "status": 200,
    "data": {
        "account": "6617186900",
        "base_money": "32.200000",
        "brokerage_money": "0.000000",
        "experience_money": "0.000000",
        "recharge_account": "0.000000",
        "recharge_money": 0,
        "withdrawal_money": 0,
        "invitation_code": "941870",
        "language": "en",
        "level": 0,
        "add_time": 1736444818,
        "total_invest_income": "0.000000",
        "financial_money": "0.000000",
        "level_start_time": 0,
        "level_end_time": 0,
        "total_task_income": "32.200000",
        "one_brokerage": "0.000000",
        "two_brokerage": "0.000000",
        "third_brokerage": "0.000000",
        "avatar": "https://t.me/i/userpic/320/7et6AQv4O8-uPEYSN0ckeLCDcABy69tki4zqHvF8uwsVvKYWSl8hGs3A72njso6o.svg",
        "one_spread_uid": 17293,
        "four_brokerage": "0.000000",
        "five_brokerage": "0.000000",
        "six_brokerage": "0.000000",
        "mining_start_time": 1736634008,
        "mining_end_time": 1736648408,
        "mining_speed": "4.02500000",
        "user_mining_time": 4,
        "tg_show_name": "somto ",
        "level_name": "VIP 0",
        "mining": "4.025000",
        "mining_time": 4,
        "invite_user": "64842****",
        "airdrop_mining_status": 2,
        "is_pwd": 0,
        "total_money": 32.2,
        "total_income": 32.2,
        "total_brokerage_income": 0,
        "total_team_count": 0
    },
    "msg": "ok"
}
```

## Received Mined Airdrop 

### Request 

```bash
curl --compressed 'https://api.assai8.com/api/user/receive_airdrop_mining' \
-X 'POST' \
-H 'Accept: application/json, text/plain, */*' \
-H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuYXNzYWk4LmNvbSIsImF1ZCI6ImFwaS5hc3NhaTguY29tIiwiaWF0IjoxNzM2NjQ3MTAzLCJuYmYiOjE3MzY2NDcxMDMsImV4cCI6MTczNzUxMTEwMywianRpIjp7ImlkIjoyMjI5OSwidHlwZSI6ImFwaSJ9fQ.ehsnnLlohHZU0F_7FYUtCJGhRi1xfUjg1xcY3_BYTks' \
-H 'Origin: https://assai8.com' \
-H 'Referer: https://assai8.com/' \
-H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Safari/605.1.15' \
-H 'Accept-Encoding: gzip, deflate, br' \
-H 'Accept-Language: en-US' \
-H 'Content-Length: 0' \
-H 'Cookie: cf_clearance=UgYJNbIj4aedMxUUgRD05rAuh8x4OCzhk1FAXe9kVj0-1736647020-1.2.1.1-_doefsuEm.iryIB07VugSWoMjWEOc7e9DeQ1vp84M.jdZ9jWSM_q0KLIUHGiAbA6hwun1RdSxDJkyEmV5XAwvTy2OcELo_npWudWBRQHrGIrxB.aV5AXq2Leaw3Euth2p3ZxxiTrY85ecMk5Qe3uTEHHMNegsOD2ilAs5XNJli9cUX7_ILR7VJSnaQygybyCGXyMkZ5w7bvthCFWU2BIgiy8Dxy_A1pNqzcf1jx3YPHjmBlwa3ynyftzVW34Cbp.wq24gZjCxJyBVhW.U6s8Zg0yjqlUPAZleBT3Qfze94c' \
-H 'Sec-Fetch-Dest: empty' \
-H 'Sec-Fetch-Mode: cors' \
-H 'Sec-Fetch-Site: same-site' \
-H 'st-lang: en' \
-H 'st-ctime: 1736650250185' \
-H 'st-ttgn: 64eca137c9eae36bd7e62914c21fb2ad'
```

### Response 

```json
{
    "status": 200,
    "data": {
        "money": "16.100000"
    },
    "msg": "Success"
}
```



## Login 

### Request 

```bash
curl 'https://api.assai8.com/api/user/tg' \
-X 'POST' \
-H 'Accept: application/json, text/plain, */*' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuYXNzYWk4LmNvbSIsImF1ZCI6ImFwaS5hc3NhaTguY29tIiwiaWF0IjoxNzM2NjU4MDIyLCJuYmYiOjE3MzY2NTgwMjIsImV4cCI6MTczNzUyMjAyMiwianRpIjp7ImlkIjoyMjI5OSwidHlwZSI6ImFwaSJ9fQ.HdbQKvxOcH1hIHqERs88_u48RLA20KFjhrDOkXyMlc8' \
-H 'Origin: https://assai8.com' \
-H 'Referer: https://assai8.com/' \
-H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Safari/605.1.15' \
-H 'Content-Length: 591' \
-H 'Accept-Encoding: gzip, deflate, br' \
-H 'Accept-Language: en-US' \
-H 'Cookie: cf_clearance=uuBW44TAjJMPLa82916T_jZyuhvqIFwGJJABTuV6sRw-1736658021-1.2.1.1-Wofw7dhu7y.yjgeiSTr57c8ISVhZC3jA67Bw1vN4fdPGOiVizhUnQ2b0IBJQPySEBuIhsEW9E91.PyBIyvTzHjXbFeQBue5EjLiuL_txiafVGEncRy_DbYWFKGjoQgssWxsd1UPqg.mC31i8Db9ayH6NqC3z9IOD6W4WMqkmCurJuO6cfRce9snGdqISDqJ_h7yh7xMkD50nkHGU_YyjgPyd.45WquQJlZ9m4cNp4CoFJZGCY__1.X8UFvPcK89vy3CsMkORdHxklCvL9Zj1Zj4cl09LXWu7MvZxG3rAUaI' \
-H 'Sec-Fetch-Dest: empty' \
-H 'Sec-Fetch-Mode: cors' \
-H 'Sec-Fetch-Site: same-site' \
-H 'st-lang: en' \
-H 'st-ctime: 1736658408650' \
-H 'st-ttgn: e5038fa25c56346cd631ef2ea14956d6' \
--data-binary '{"init_data":"query_id=AAFUQmoKAwAAAFRCago_xFME&user=%7B%22id%22%3A6617186900%2C%22first_name%22%3A%22somto%22%2C%22last_name%22%3A%22%22%2C%22username%22%3A%22i_am_joe_rogan%22%2C%22language_code%22%3A%22en%22%2C%22allows_write_to_pm%22%3Atrue%2C%22photo_url%22%3A%22https%3A%5C%2F%5C%2Ft.me%5C%2Fi%5C%2Fuserpic%5C%2F320%5C%2F7et6AQv4O8-uPEYSN0ckeLCDcABy69tki4zqHvF8uwsVvKYWSl8hGs3A72njso6o.svg%22%7D&auth_date=1736658015&signature=pw_PK2dqmfDVuaMfXnm1abiuQ2RXj9TqCpdaHm9EFUiFSuaSCLA4CbR10B0YWEMtgDP_-tc_eK6wNtYwtXvaCw&hash=b894dfa6c7c6775dc5e6b04ef714f2585a88d1dc1e62236d6bbd3ff1ce32068d"}'
```
