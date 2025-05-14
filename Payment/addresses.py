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

urls = {
    vars.the_coins[0]: vars.other_vars["VERIFY_SITE"] + "/avalanche" + vars.other_vars["VERIFY_SITE_SEPARATOR"],
    vars.the_coins[1]: vars.other_vars["VERIFY_SITE"] + "/bnb" + vars.other_vars["VERIFY_SITE_SEPARATOR"],
    vars.the_coins[2]: vars.other_vars["VERIFY_SITE"] + "/bitcoin" + vars.other_vars["VERIFY_SITE_SEPARATOR"],
    vars.the_coins[3]: vars.other_vars["VERIFY_SITE"] + "/bitcoin-cash" + vars.other_vars["VERIFY_SITE_SEPARATOR"],
    vars.the_coins[4]: vars.other_vars["VERIFY_SITE"] + "/cardano" + vars.other_vars["VERIFY_SITE_SEPARATOR"],
    vars.the_coins[5]: vars.other_vars["VERIFY_SITE"] + "/dash" + vars.other_vars["VERIFY_SITE_SEPARATOR"],
    vars.the_coins[6]: vars.other_vars["VERIFY_SITE"] + "/digibyte" + vars.other_vars["VERIFY_SITE_SEPARATOR"],
    vars.the_coins[7]: vars.other_vars["VERIFY_SITE"] + "/dogecoin" + vars.other_vars["VERIFY_SITE_SEPARATOR"],
    vars.the_coins[8]: vars.other_vars["VERIFY_SITE"] + "/ethereum" + vars.other_vars["VERIFY_SITE_SEPARATOR"],
    vars.the_coins[9]: vars.other_vars["VERIFY_SITE"] + "/groestlcoin" + vars.other_vars["VERIFY_SITE_SEPARATOR"],
    vars.the_coins[10]: vars.other_vars["VERIFY_SITE"] + "/litecoin" + vars.other_vars["VERIFY_SITE_SEPARATOR"],
    vars.the_coins[11]: vars.other_vars["VERIFY_SITE"] + "/polkadot" + vars.other_vars["VERIFY_SITE_SEPARATOR"],
    vars.the_coins[12]: vars.other_vars["VERIFY_SITE"] + "/solana" + vars.other_vars["VERIFY_SITE_SEPARATOR"],
    vars.the_coins[13]: vars.other_vars["VERIFY_SITE"] + "/stellar" + vars.other_vars["VERIFY_SITE_SEPARATOR"],
    vars.the_coins[14]: vars.other_vars["VERIFY_SITE"] + "/ton" + vars.other_vars["VERIFY_SITE_SEPARATOR"],
    vars.the_coins[15]: vars.other_vars["VERIFY_SITE"] + "/tron" + vars.other_vars["VERIFY_SITE_SEPARATOR"],
}


def update_urls():
    urls.clear()
    urls.update({
        vars.the_coins[0]: vars.other_vars["VERIFY_SITE"] + "/avalanche" + vars.other_vars["VERIFY_SITE_SEPARATOR"],
        vars.the_coins[1]: vars.other_vars["VERIFY_SITE"] + "/bnb" + vars.other_vars["VERIFY_SITE_SEPARATOR"],
        vars.the_coins[2]: vars.other_vars["VERIFY_SITE"] + "/bitcoin" + vars.other_vars["VERIFY_SITE_SEPARATOR"],
        vars.the_coins[3]: vars.other_vars["VERIFY_SITE"] + "/bitcoin-cash" + vars.other_vars["VERIFY_SITE_SEPARATOR"],
        vars.the_coins[4]: vars.other_vars["VERIFY_SITE"] + "/cardano" + vars.other_vars["VERIFY_SITE_SEPARATOR"],
        vars.the_coins[5]: vars.other_vars["VERIFY_SITE"] + "/dash" + vars.other_vars["VERIFY_SITE_SEPARATOR"],
        vars.the_coins[6]: vars.other_vars["VERIFY_SITE"] + "/digibyte" + vars.other_vars["VERIFY_SITE_SEPARATOR"],
        vars.the_coins[7]: vars.other_vars["VERIFY_SITE"] + "/dogecoin" + vars.other_vars["VERIFY_SITE_SEPARATOR"],
        vars.the_coins[8]: vars.other_vars["VERIFY_SITE"] + "/ethereum" + vars.other_vars["VERIFY_SITE_SEPARATOR"],
        vars.the_coins[9]: vars.other_vars["VERIFY_SITE"] + "/groestlcoin" + vars.other_vars["VERIFY_SITE_SEPARATOR"],
        vars.the_coins[10]: vars.other_vars["VERIFY_SITE"] + "/litecoin" + vars.other_vars["VERIFY_SITE_SEPARATOR"],
        vars.the_coins[11]: vars.other_vars["VERIFY_SITE"] + "/polkadot" + vars.other_vars["VERIFY_SITE_SEPARATOR"],
        vars.the_coins[12]: vars.other_vars["VERIFY_SITE"] + "/solana" + vars.other_vars["VERIFY_SITE_SEPARATOR"],
        vars.the_coins[13]: vars.other_vars["VERIFY_SITE"] + "/stellar" + vars.other_vars["VERIFY_SITE_SEPARATOR"],
        vars.the_coins[14]: vars.other_vars["VERIFY_SITE"] + "/ton" + vars.other_vars["VERIFY_SITE_SEPARATOR"],
        vars.the_coins[15]: vars.other_vars["VERIFY_SITE"] + "/tron" + vars.other_vars["VERIFY_SITE_SEPARATOR"],
    })


# List of cryptocurrency names
cryptos = {
    vars.the_coins[0]: "Payment/Photos/avalanche (avax).png",
    vars.the_coins[1]: "Payment/Photos/binance coin (bnb).png",
    vars.the_coins[2]: "Payment/Photos/bitcoin (btc).png",
    vars.the_coins[3]: "Payment/Photos/bitcoin cash (bch).png",
    vars.the_coins[4]: "Payment/Photos/cardano (ada).png",
    vars.the_coins[5]: "Payment/Photos/dash (dash).png",
    vars.the_coins[6]: "Payment/Photos/digibyte (dgb).png",
    vars.the_coins[7]: "Payment/Photos/dogecoin (doge).png",
    vars.the_coins[8]: "Payment/Photos/ethereum (eth).png",
    vars.the_coins[9]: "Payment/Photos/groestlcoin (grs).png",
    vars.the_coins[10]: "Payment/Photos/litecoin (ltc).png",
    vars.the_coins[11]: "Payment/Photos/polkadot (dot).png",
    vars.the_coins[12]: "Payment/Photos/solana (sol).png",
    vars.the_coins[13]: "Payment/Photos/stellar (xlm).png",
    vars.the_coins[14]: "Payment/Photos/toncoin (ton).png",
    vars.the_coins[15]: "Payment/Photos/tron (trx).png",
}
