import Payment.iap_variables as vars

addresses = {
    vars.the_coins[0]: "0x987da2d7b222a422d6605c66a6e47aeabf3e91c5",
    vars.the_coins[1]: "bnb12uygta8tlnhdr3vlgw5rtcwwsrm2qgu6hu3t0h",
    vars.the_coins[2]: "1LQSzFZKE5vwiUS94toMG7r5M2nQ4X2muw",
    vars.the_coins[3]: "qzhr6lc9r64c3wg3jnndqaxzpyxeghdp2s57w5wgwu",
    vars.the_coins[4]: "DdzFFzCqrht3N125qEXgFCb1KGrcusTaL8dKW7Ep39zpV8919ZKxn6GkWYSEpaPfoY4MyfogozfLUTpVyKdTmnZP6bZSV94Lhv9GuXm9",
    vars.the_coins[5]: "Xn5HwktiWJfgKydTDjodBTjJDA6tVxzAho",
    vars.the_coins[6]: "D97CQ5pV1AukRY1FJTSW3CFkJtUZgdwJq4",
    vars.the_coins[7]: "D5YP7CggUUkS3fu1B7RjhjJ7jvNu6A4Ksx",
    vars.the_coins[8]: "0x80D3CA7528cF05118131dBa3d7852Db2685c4b9E",
    vars.the_coins[9]: "Fafh4zcRBiZiZ1ZqVgk5u6C1hzWJfSWrBf",
    vars.the_coins[10]: "LRQ6TBVXsEVPApbCY79bV1d9LR8E7JiuDd",
    vars.the_coins[11]: "12b7ww2zhuZsMvNgDRTuQaC3sK7wEVyRjoeLdsxHeLCuLyt8",
    vars.the_coins[12]: "Feyknn2ehnUc5b9CvgogFS8wehvZzS9FWaxcAANnGz7g",
    vars.the_coins[13]: "GCZI74FS6WJDIQUMIJQBDIOCZMNCBGCWJ6AA6QO45Y5LA7DJ5L2ARCWT",
    vars.the_coins[14]: "UQDdP6a_0IdInRtVbCAMO5cSIU6c1ptVegeKewPltXGJVsGO",
    vars.the_coins[15]: "TEivYaNov8LERnBaTJiry8K9m7u46Mxs86",
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
