Since most likely I won't have enough time to finish this project I though
why don't I experiment a little and walk you through, the process.
Also after few years I'll look back to this and think, Oh that's some garbage code,
and continute writeing code that I  will condiser garbage after few years.

First stage:
manually examining data.
thoughts:
1. That's a lot of columns for this tiny dataset
2. Structured data, it's been a long time since we last met.
3. Cool there are overwelmingly more Succsesses than failures, I'm gonna have
problems because of imbalanced dataset.
4. I'm gonna do some boring job examining which column to encode with one hot etc

Second stage:
1. loading data, and going to docs to see that it's not load_csv, neither from_csv
but read_csv, pandas why would you do this to me
2. Droping unneeded columns
3. Encoding data so that I can feed it to algorithm

Turns out there are a lt of missing values which i can't just drop because they
are a huge part of the data, so I'll need to find a good way to handle them

Also I just realised that i have never dealed with both categorical and numerical
data simultanionly so I'm gonna learn a lot of thing.

Also encoding data is quite boring, I just remembered a joke.
Data scientists spend 20 percent of the time prepairing data,
and 80 percent complaining tha they need to prepare data.

For encoding I decided to seperate dataframe by datatypes, use one hot encoder
and binary encoder, and for handling numericals i will normalize them.
That's maybe not the best aproach but it's good to experiment.

I decided to manually select more columns to delete,
for example Short Description of company profile varies to much and roughly said
it's unique for every company, just like companies name, so it won't benefit the algorithm

Surprise! for example Team size all employees has dtype 'object' since there are
some "No info"s
