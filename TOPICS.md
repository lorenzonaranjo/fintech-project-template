# Project topics

Each group picks one topic on the Canvas sign-up for its section. Within a section, every topic goes to one group only. A group may propose its own topic instead, with the instructor's approval, by March 30.

Each brief gives the question, where to start reading, data that are free and were tested in November 2026, and one idea for the figure. The references are a starting point: you must read what you cite, and you will need more sources than these.

**For every topic:**

- Save the data you download in `data/` and record the source and date in `data/README.md`. Free APIs change without notice; the page must still render from your saved copy.
- `yfinance` is an unofficial tool for Yahoo Finance data. It works today but can break.
- The SEC's EDGAR refuses requests without a `User-Agent` header that names you and gives an email address, for example `{"User-Agent": "Jane Doe jdoe@wustl.edu"}`. Keep below 10 requests a second.
- FRED series download without a key as CSV from `https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS2,DGS10` (any series IDs, comma-separated).
- Topics marked **harder** need more programming (an API key, decoding blockchain data, or a machine learning model). They suit a group with a strong programmer.

## Blockchain

### 1. Bitcoin mining after the halvings

**Question.** Every four years the reward for mining a Bitcoin block halves. What happens to miners' revenue, the hash rate and the difficulty, and what does that say about how secure the network can stay as rewards shrink?

**Start with.** Budish, Eric (2025), "Trust at Scale: The Economic Limits of Cryptocurrencies and Blockchains," *Quarterly Journal of Economics* 140(1), 1–62, <https://doi.org/10.1093/qje/qjae033>. An earlier version is NBER Working Paper 24717 (2018), "The Economic Limits of Bitcoin and the Blockchain."

**Data (free, no key).** mempool.space, <https://mempool.space/docs/api/rest>: `https://mempool.space/api/v1/mining/hashrate/all` gives daily hash rate and difficulty since 2009. Blockchain.com charts, <https://www.blockchain.com/explorer/docs>: `https://api.blockchain.info/charts/miners-revenue?timespan=all&sampled=false&format=json` gives daily miner revenue in USD (without `sampled=false` you get one point every few days).

**Figure.** Daily miner revenue in USD, which is what the network pays for its security, with the 2016, 2020 and 2024 halvings marked. Revenue per unit of hash rate is a different measure: competition pushes it toward miners' cost per hash, so it says little about security.

### 2. Ethereum's move to proof of stake

**Question.** In September 2022 Ethereum replaced mining with staking (the Merge). What changed for the supply of ether, for what stakers earn, and for the network's energy use?

**Start with.** Saleh, Fahad (2021), "Blockchain without Waste: Proof-of-Stake," *Review of Financial Studies* 34(3), 1156–1190, <https://doi.org/10.1093/rfs/hhaa075>. It is a theory paper: it explains why proof of stake can reach consensus without spending energy and why the reward should be modest. It does not model Ethereum's actual design or use data. For energy: Crypto Carbon Ratings Institute (2022), "The Merge: Implications on the Electricity Consumption and Carbon Footprint of the Ethereum Network," <https://carbon-ratings.com/eth-report-2022>.

**Data (free, no key).** ETH supply: `https://ultrasound.money/api/v2/fees/supply-over-time` (works, but the API is undocumented). Staking yield: DefiLlama, `https://yields.llama.fi/chart/747c1d2a-c668-4682-b9f9-296708a3dd90` (Lido stETH, daily APY since May 2022). Avoid beaconcha.in, which now needs a paid key.

**Figure.** ETH supply since August 2021 with the Merge marked, next to the staking yield.

### 3. Spot Bitcoin ETFs

**Question.** Since January 2024, investors can buy Bitcoin through exchange-traded funds. How closely do the funds track Bitcoin, what do they charge, and how fast did they grow?

**Start with.** Gensler, Gary (2024), "Statement on the Approval of Spot Bitcoin Exchange-Traded Products," U.S. Securities and Exchange Commission, January 10, 2024, <https://www.sec.gov/news/statement/gensler-statement-spot-bitcoin-011023>.

**Data.** Prices: `yfinance` for IBIT, FBTC, GBTC and BTC-USD. Growth: SEC EDGAR (no key, User-Agent required), `https://data.sec.gov/api/xbrl/companyfacts/CIK0001980994.json` (IBIT), which has quarterly shares outstanding. Fees: the funds' own pages. Daily flow tables (such as Farside Investors) block scripts; copy them by hand if you use them.

**Figure.** Daily returns of IBIT and GBTC against Bitcoin's, or IBIT's quarterly shares outstanding.

### 4. Is Bitcoin a risk asset?

**Question.** Over 2011 to 2018, crypto returns showed no statistically significant exposure to stocks. Has that changed, and when?

**Start with.** Adrian, Tobias, Tara Iyer and Mahvash S. Qureshi (2022), "Crypto Prices Move More in Sync With Stocks, Posing New Risks," IMF Blog, January 11, 2022, <https://www.imf.org/en/blogs/articles/2022/01/11/crypto-prices-move-more-in-sync-with-stocks-posing-new-risks>. Liu, Yukun and Aleh Tsyvinski (2021), "Risks and Returns of Cryptocurrency," *Review of Financial Studies* 34(6), 2689–2727, <https://doi.org/10.1093/rfs/hhaa113>.

**Data (free, no key).** `yfinance` for BTC-USD, SPY and QQQ. Bitcoin trades every day; compute returns over stock-market trading days only.

**Figure.** Rolling 90-day correlation of daily Bitcoin and S&P 500 returns.

### 5. Paying for blockspace: Bitcoin transaction fees

**Question.** Bitcoin users bid for limited space in each block. When is that space congested, what do fees do then, and can fees replace the block reward in paying miners?

**Start with.** Easley, David, Maureen O'Hara and Soumya Basu (2019), "From Mining to Markets: The Evolution of Bitcoin Transaction Fees," *Journal of Financial Economics* 134(1), 91–109, <https://doi.org/10.1016/j.jfineco.2019.03.004>. Huberman, Gur, Jacob D. Leshno and Ciamac Moallemi (2021), "Monopoly without a Monopolist: An Economic Analysis of the Bitcoin Payment System," *Review of Economic Studies* 88(6), 3011–3040, <https://doi.org/10.1093/restud/rdab014>.

**Data (free, no key).** `https://api.blockchain.info/charts/transaction-fees-usd?timespan=all&sampled=false&format=json` (daily total fees in USD). mempool.space, `https://mempool.space/api/v1/mining/blocks/fee-rates/1y` (fee-rate percentiles). Stay with Bitcoin: Ethereum's fee history needs a paid Etherscan plan.

**Figure.** Daily total fees and fees as a share of miner revenue, with periods of congestion marked by a measure that does not use fees, such as how full blocks are or the number of transactions waiting.

### 6. Bitcoin in a portfolio

**Question.** Does adding a little Bitcoin to a stock and bond portfolio lower its risk or raise it? Find the Bitcoin weight at which the portfolio's risk is lowest, if there is one, and see how it changed as Bitcoin's correlation with stocks rose.

**Start with.** Liu, Yukun and Aleh Tsyvinski (2021), "Risks and Returns of Cryptocurrency," *Review of Financial Studies* 34(6), 2689–2727, <https://doi.org/10.1093/rfs/hhaa113>, for crypto's volatility and its low exposure to stocks up to 2018. The paper does not study portfolio weights; the course notes on diversification do.

**Data (free, no key).** `yfinance` for BTC-USD, SPY and AGG. Backup for Bitcoin: FRED series `CBBTCUSD`.

**Figure.** Portfolio volatility against Bitcoin's weight, from 0 to 20% of a 60/40 stock-bond portfolio, estimated before 2020 and after. Whether an asset lowers risk depends on its weight given its correlation; the figure should show both.

## Stablecoins and tokenization

### 7. The USDC depeg during the Silicon Valley Bank run

**Question.** In March 2023, USDC fell well below one dollar for a weekend after its issuer reported deposits at the failed Silicon Valley Bank. Why does a stablecoin backed by dollar assets (bank deposits and Treasury bills) trade below one dollar, and why did this one recover?

**Start with.** Circle (2023), "$3.3 Billion of USDC Reserve Risk Removed, Dollar De-peg Closes," press release, March 13, 2023, <https://www.circle.com/es/pressroom/3-3-billion-of-usdc-reserve-risk-removed-dollar-de-peg-closes>. Ma, Yiming, Yao Zeng and Anthony Lee Zhang (2026), "Stablecoin Runs and the Centralization of Arbitrage," *Review of Financial Studies*, advance article, <https://doi.org/10.1093/rfs/hhag072> (earlier version: NBER Working Paper 33882, 2025). Their data end before the depeg; the recovery followed the guarantee of all Silicon Valley Bank deposits on March 12, 2023, so read the press release and news for that part.

**Data (free, no key).** Hourly USDC/USD from Bitstamp, <https://www.bitstamp.net/api/>: `https://www.bitstamp.net/api/v2/ohlc/usdcusd/?step=3600&limit=1000&start=1678320000&end=1678838400` (March 9 to 15, 2023). Daily prices: `yfinance` USDC-USD. CoinGecko's free API cannot reach back to 2023.

**Figure.** Hourly USDC price from March 9 to 15, 2023, with the news events marked.

### 8. What backs a stablecoin?

**Question.** What do the largest stablecoins hold as reserves, and what does the GENIUS Act of 2025 now require them to hold?

**Start with.** The GENIUS Act: Guiding and Establishing National Innovation for U.S. Stablecoins Act, Public Law 119-27, signed July 18, 2025, <https://www.govinfo.gov/app/details/PLAW-119publ27>. Gorton, Gary B. and Jeffery Y. Zhang (2023), "Taming Wildcat Stablecoins," *University of Chicago Law Review* 90(3), 909–971, <https://chicagounbound.uchicago.edu/uclrev/vol90/iss3/3>.

**Data.** Supply over time (free, no key): DefiLlama, `https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=2` (USDC; `stablecoin=1` is USDT). Reserves: the monthly attestation PDFs at <https://www.circle.com/transparency> and Tether's reports at <https://tether.to/en/transparency/>; type in the numbers by hand.

**Figure.** USDC and USDT supply over time, and the composition of each one's reserves on one date.

### 9. Tokenized Treasuries and money market funds

**Question.** Funds such as BlackRock's BUIDL put shares of Treasury-bill funds on a blockchain. What problem does that solve, for whom, and how fast is it growing?

**Start with.** Committee on Payments and Market Infrastructures (2024), "Tokenisation in the context of money and other assets: concepts and implications for central banks," Bank for International Settlements, <https://www.bis.org/cpmi/publ/d225.htm>. Financial Stability Board (2024), "The Financial Stability Implications of Tokenisation," <https://www.fsb.org/uploads/P221024-2.pdf>.

**Data (free, no key, last 365 days only).** CoinGecko, `https://api.coingecko.com/api/v3/coins/blackrock-usd-institutional-digital-liquidity-fund/market_chart?vs_currency=usd&days=365` (BUIDL's daily market value). FRED `DTB3` for the T-bill yield. rwa.xyz has the whole market but needs an account, and most of its data are paid.

**Figure.** BUIDL's market value over the last year against the 3-month T-bill yield.

### 10. Stablecoins versus central bank digital currencies

**Question.** Many central banks are exploring digital currencies, while in the United States a 2025 executive order barred federal agencies from work on one and the GENIUS Act regulated private stablecoins instead. What are the two models, and where is each one advancing?

**Start with.** Auer, Raphael, Giulio Cornelli and Jon Frost (2023), "Rise of the Central Bank Digital Currencies," *International Journal of Central Banking* 19(4), 185–214, <https://www.ijcb.org/journal/v19n4/rise-central-bank-digital-currencies>. Executive Order 14178, "Strengthening American Leadership in Digital Financial Technology," January 23, 2025, 90 Fed. Reg. 8647, <https://www.federalregister.gov/documents/2025/01/31/2025-02123> (Section 5 prohibits a U.S. CBDC). For the comparison of the two models, Table 1 of Gorton and Zhang (2023), cited in topic 8.

**Data (free, no key).** CBDC projects by country: the BIS dataset of Auer, Cornelli and Frost, updated to March 2024, <https://www.bis.org/publications/bis-working-paper/work880-data-mar2024.xlsx>. Stablecoins: DefiLlama, `https://stablecoins.llama.fi/stablecoincharts/all` (total supply). The Atlantic Council's CBDC tracker has no download.

**Figure.** Total stablecoin supply over time, next to the countries whose CBDC projects are furthest along (research, pilot or launched). Supply measures use and the project index measures stage of development; say so on the page.

## Decentralized finance

### 11. Providing liquidity on Uniswap: fees versus losses to arbitrageurs

**Question.** Liquidity providers on an automated market maker earn trading fees but lose to arbitrageurs, who trade against the pool whenever the market price moves. For an actual pool, did the fees cover that loss?

**Start with.** Lehar, Alfred and Christine Parlour (2025), "Decentralized Exchange: The Uniswap Automated Market Maker," *Journal of Finance* 80(1), 321–374, <https://doi.org/10.1111/jofi.13405>. Milionis, Jason, Ciamac C. Moallemi, Tim Roughgarden and Anthony Lee Zhang (2022), "Automated Market Making and Loss-Versus-Rebalancing," working paper (2022, revised 2026), <https://arxiv.org/abs/2208.06046>. They explain why the popular "impermanent loss" is a poor measure (it depends on the start date you pick) and propose loss-versus-rebalancing instead, about σ²/8 of the pool's value per unit of time for a constant-product pool.

**Data (free, no key).** DefiLlama, `https://yields.llama.fi/chart/665dc8bc-c79d-4800-97f7-304bf368e547` (Uniswap v3 USDC-WETH 0.05% pool: daily value locked and fee yield since 2022). ETH price from `yfinance` (ETH-USD) for the variance. This is a Uniswap v3 pool, where liquidity can be concentrated in a price range; the papers study constant-product pools, so assume a full-range position, which behaves like one, and note that the pool-wide fee yield may overstate what such a position earns. Dune and The Graph are no longer practical for free.

**Figure.** Cumulative fee income against cumulative loss-versus-rebalancing, and, for comparison, the impermanent loss of a position opened on a date you choose.

### 12. Liquidations in DeFi lending (harder)

**Question.** On lending protocols such as Aave, a loan becomes eligible for liquidation when its collateral falls too far in value, and anyone (in practice, bots) can then repay part of the debt and take collateral at a discount. What happened during a sharp crash, and who earned the liquidation bonuses?

**Start with.** Qin, Kaihua, Liyi Zhou, Pablo Gamito, Philipp Jovanovic and Arthur Gervais (2021), "An Empirical Study of DeFi Liquidations: Incentives, Risks, and Instabilities," *Proceedings of the 21st ACM Internet Measurement Conference*, 336–350, <https://doi.org/10.1145/3487552.3487811>. Their data end in April 2021 and cover earlier versions of Aave, whose liquidation terms differ from Aave V3's.

**Data (free key from an Etherscan account).** Etherscan logs API, <https://docs.etherscan.io/etherscan-v2/api-endpoints/logs>: `LiquidationCall` events of the Aave V3 pool (address `0x87870Bca3F3fD6335C3F4ce8392D69350B4fA4E2`, topic0 `0xe413a321e8681d831f4dbccbca790d2952b56f977908e45be37335533e005286`). At most 1,000 events per call, so query in block ranges. A crash to study: October 10 to 11, 2025. Decoding the amounts takes some work with the contract's ABI.

**Figure.** Liquidations per hour during the crash, against the ETH price.

### 13. Prediction markets: prices as probabilities

**Question.** On Kalshi and Polymarket, a contract pays one dollar if an event happens. Can its price be read as a probability (strictly, a risk-neutral probability), and did the two markets agree on the 2024 U.S. presidential election?

**Start with.** Wolfers, Justin and Eric Zitzewitz (2004), "Prediction Markets," *Journal of Economic Perspectives* 18(2), 107–126, <https://doi.org/10.1257/0895330041371321>, including their caveats: the favorite–long-shot bias and thin markets. On regulation: *KalshiEX LLC v. Commodity Futures Trading Commission*, No. 1:23-cv-03257 (D.D.C., September 2024), which allowed Kalshi to list contracts on control of Congress, <https://storage.courtlistener.com/recap/gov.uscourts.dcd.261465/gov.uscourts.dcd.261465.47.0.pdf>.

**Data (free, no key).** Polymarket: `https://gamma-api.polymarket.com/events?slug=presidential-election-winner-2024` gives each outcome's token ID; then `https://clob.polymarket.com/prices-history?market=<token ID>&interval=max&fidelity=1440` gives daily prices. Docs: <https://docs.polymarket.com/developers/CLOB/timeseries>. Kalshi: `https://api.elections.kalshi.com/trade-api/v2/historical/markets/PRES-2024-DJT/candlesticks?start_ts=1727740800&end_ts=1731024000&period_interval=1440`. Docs: <https://docs.kalshi.com/getting_started/historical_data>.

**Figure.** The two markets' prices for the same outcome on one plot, through election night.

## Neural networks and language models

### 14. Neural networks versus Black-Scholes (harder)

**Question.** Can a neural network trained on market prices price options better than the Black-Scholes formula, and where does it do better or worse?

**Start with.** Hutchinson, James M., Andrew W. Lo and Tomaso Poggio (1994), "A Nonparametric Approach to Pricing and Hedging Derivative Securities via Learning Networks," *Journal of Finance* 49(3), 851–889, <https://doi.org/10.1111/j.1540-6261.1994.tb00081.x>. The course notebook on option pricing with neural networks.

**Data (free, no key).** `yfinance`: `yf.Ticker("SPY").option_chain(expiry)` for each expiry in `yf.Ticker("SPY").options`. This gives today's prices only, which is enough: train on today's cross-section of strikes and maturities. Use the bid-ask midpoint, and drop quotes with a zero bid or an old last trade. Free historical option data do not exist.

**Figure.** Pricing errors on strikes and maturities held out of training, for the network and for Black-Scholes with a single volatility (at-the-money implied or historical), by moneyness and maturity. Black-Scholes with each option's own implied volatility fits perfectly by construction, so it is not a fair benchmark. Hutchinson, Lo and Poggio instead train on six months of prices and test hedging over the next six; with one day of data you test how well the network fills in the volatility smile. SPY options are American and SPY pays dividends; say how you handle both.

### 15. Predicting stock returns with machine learning (harder)

**Question.** Does a machine learning model predict the stock market's excess return better, out of sample, than the historical mean and a linear predictive regression?

**Start with.** Welch, Ivo and Amit Goyal (2008), "A Comprehensive Look at the Empirical Performance of Equity Premium Prediction," *Review of Financial Studies* 21(4), 1455–1508, <https://doi.org/10.1093/rfs/hhm014>. Gu, Shihao, Bryan Kelly and Dacheng Xiu (2020), "Empirical Asset Pricing via Machine Learning," *Review of Financial Studies* 33(5), 2223–2273, <https://doi.org/10.1093/rfs/hhaa009>. Welch and Goyal find that linear predictive regressions do not beat the historical mean out of sample. Gu, Kelly and Xiu forecast individual stocks with licensed CRSP and Compustat data and get their S&P 500 forecasts by adding up the stock forecasts; with free data you forecast the market directly from Welch and Goyal's predictors, which Gu, Kelly and Xiu also use.

**Data (free, no key).** Amit Goyal's predictor data, updated through 2025, from <https://sites.google.com/view/agoyal145> (the "Updated data" file under Welch and Goyal 2008). Ken French Data Library, <https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html>.

**Figure.** Cumulative squared forecast error of the historical mean minus that of each model, over time, in the style of Welch and Goyal.

### 16. Reading the Fed with a language model

**Question.** Can a language model read what a Federal Reserve statement says about future policy, and do Treasury yields move with it on announcement days?

**Start with.** Gürkaynak, Refet S., Brian Sack and Eric T. Swanson (2005), "Do Actions Speak Louder Than Words? The Response of Asset Prices to Monetary Policy Actions and Statements," *International Journal of Central Banking* 1(1), 55–93, <https://www.ijcb.org/journal/v1n1/do-actions-speak-louder-words-response-asset-prices-monetary-policy-actions-and>: statements move longer-term Treasury yields more than rate decisions do. Lucca, David O. and Francesco Trebbi (2009), "Measuring Central Bank Communication: An Automated Approach with Application to FOMC Statements," NBER Working Paper 15367, <https://www.nber.org/papers/w15367>: an automated score of statements, related to Treasury yields. For measuring tone with a finance dictionary: Shapiro, Adam Hale and Daniel J. Wilson (2022), "Taking the Fed at its Word: A New Approach to Estimating Central Bank Objectives using Text Analysis," *Review of Economic Studies* 89(5), 2768–2805, <https://doi.org/10.1093/restud/rdab094> (they study transcripts and minutes to estimate the Fed's objectives, not market reactions).

**Data (free, no key).** FOMC statements: <https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm> and, for earlier years, <https://www.federalreserve.gov/monetarypolicy/fomc_historical_year.htm>; each statement is at `https://www.federalreserve.gov/newsevents/pressreleases/monetaryYYYYMMDDa.htm`. Yields: FRED `DGS2` and `DGS10`.

**Figure.** Change in the 10-year yield on each announcement day against the change in the statement's score for future policy. Two cautions: a gloomy statement is usually dovish, so negative tone is not the same as a hawkish signal; and yields also react to the rate decision itself and to other news that day, so separate days with a rate change from days without.

### 17. What firms say about AI in their 10-K filings

**Question.** How often do U.S. public companies mention artificial intelligence in their annual reports, and how has that changed since ChatGPT?

**Start with.** Loughran, Tim and Bill McDonald (2011), "When Is a Liability Not a Liability? Textual Analysis, Dictionaries, and 10-Ks," *Journal of Finance* 66(1), 35–65, <https://doi.org/10.1111/j.1540-6261.2010.01625.x>. Babina, Tania, Anastassia Fedyk, Alex He and James Hodson (2024), "Artificial Intelligence, Firm Growth, and Product Innovation," *Journal of Financial Economics* 151, 103745, <https://doi.org/10.1016/j.jfineco.2023.103745> (they measure AI investment from workers' resumes and job postings, not from filings, and warn that keyword lists produce errors both ways). Loughran and McDonald's lesson is that the meaning of a word depends on context; a mention of AI in a 10-K measures what a firm says, often in boilerplate risk factors, not what it invests.

**Data (free, no key, User-Agent required).** SEC EDGAR APIs, <https://www.sec.gov/search-filings/edgar-application-programming-interfaces>, and full-text search, <https://www.sec.gov/edgar/search/> (filings since 2001).

**Figure.** Share of 10-K filings that mention "artificial intelligence," by year.

### 18. Algorithms, lending and fairness in mortgage data

**Question.** Do mortgage approval rates differ across groups of borrowers, and what do studies with richer data find about whether algorithms in lending make gaps smaller or larger?

**Start with.** Bartlett, Robert, Adair Morse, Richard Stanton and Nancy Wallace (2022), "Consumer-Lending Discrimination in the FinTech Era," *Journal of Financial Economics* 143(1), 30–56, <https://doi.org/10.1016/j.jfineco.2021.05.047>. Fuster, Andreas, Paul Goldsmith-Pinkham, Tarun Ramadorai and Ansgar Walther (2022), "Predictably Unequal? The Effects of Machine Learning on Credit Markets," *Journal of Finance* 77(1), 5–47, <https://doi.org/10.1111/jofi.13090>. Both papers add proprietary loan data to HMDA. Bartlett et al. find that minority borrowers pay higher interest rates at the same credit risk, with smaller gaps at fintech lenders for FHA loans; Fuster et al. predict that machine-learning credit models would leave the approval gap about unchanged but widen gaps in rates. Neither paper's main result is about denials.

**Data (free, no key).** HMDA Data Browser API, <https://ffiec.cfpb.gov/documentation/api/data-browser/>. For example, `https://ffiec.cfpb.gov/v2/data-browser-api/view/aggregations?msamds=41180&years=2024&actions_taken=1,3&races=White,Black%20or%20African%20American` counts originated (1) and denied (3) applications by race in the St. Louis area. The public data do not include credit scores, so a raw gap in approvals is not by itself evidence of discrimination; the page must say what else could explain it.

**Figure.** Denial rates by group across metropolitan areas or years.
