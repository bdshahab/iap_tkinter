import Payment.iap_variables as vars

addresses = {
    vars.the_coins[0]: "1LQSzFZKE5vwiUS94toMG7r5M2nQ4X2muw",
    vars.the_coins[1]: "qzhr6lc9r64c3wg3jnndqaxzpyxeghdp2s57w5wgwu",
    vars.the_coins[2]: "Xn5HwktiWJfgKydTDjodBTjJDA6tVxzAho",
    vars.the_coins[3]: "D97CQ5pV1AukRY1FJTSW3CFkJtUZgdwJq4",
    vars.the_coins[4]: "D5YP7CggUUkS3fu1B7RjhjJ7jvNu6A4Ksx",
    vars.the_coins[5]: "qqmrrza2rgxur2slmgu4q9l3tql0j65ravuhg3c6r5",
    vars.the_coins[6]: "Fafh4zcRBiZiZ1ZqVgk5u6C1hzWJfSWrBf",
    vars.the_coins[7]: "LRQ6TBVXsEVPApbCY79bV1d9LR8E7JiuDd",
    vars.the_coins[8]: "TEivYaNov8LERnBaTJiry8K9m7u46Mxs86",
}

urls = {}
for coin in vars.the_coins:
    urls[coin] = vars.other_vars["VERIFY_SITE"] + \
        vars.other_vars[coin] + vars.other_vars["VERIFY_SITE_SEPARATOR"]


def update_urls():
    urls.clear()
    for coin in vars.the_coins:
        urls[coin] = vars.other_vars["VERIFY_SITE"] + \
            vars.other_vars[coin] + vars.other_vars["VERIFY_SITE_SEPARATOR"]


cryptos = {}
for coin in vars.the_coins:
    cryptos[coin] = f"Payment/Photos/{coin.lower()}.png"
