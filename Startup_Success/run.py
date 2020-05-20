import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import ExtraTreesClassifier
# from sklearn.pipeline import make_pipeline

data = pd.read_csv("data.csv", engine='python')

# extracting labels
# NOTE: positive class indicates sucesses
labels = data["Dependent-Company Status"]
le = LabelEncoder()
le.fit(labels)
labels = le.transform(labels)

# deleting unneeded colums
del data["Company_Name"]
del data["Dependent-Company Status"]
del data["Short Description of company profile"]
del data['Investors']

#/////////////////////// NUMERICALS       ////////////////////

numericals_columns = ["year of founding", "Age of company in years", "Internet Activity Score", "Employee Count", "Employees count MoM change", "Number of Investors in Seed", "Number of Investors in Angel and or VC", "Number of Co-founders", "Number of of advisors", "Team size Senior leadership", "Team size all employees", "Number of of repeat investors",
                      "Percent_skill_Entrepreneurship", "Percent_skill_Operations", "Percent_skill_Engineering", "Percent_skill_Marketing", "Percent_skill_Leadership", "Percent_skill_Data Science", "Percent_skill_Business Strategy", "Percent_skill_Product Management", "Percent_skill_Sales", "Percent_skill_Domain", "Percent_skill_Law", "Percent_skill_Consulting", "Percent_skill_Finance", "Percent_skill_Investment", "Renown score", "Number of Direct competitors", "Employees per year of company existence", "Number of Recognitions for Founders and Co-founders",  "Last round of funding received (in milionUSD)", "Time to 1st investment (in months)", "Avg time to investment - average across all rounds, measured from previous investment", "google page rank of company website"]


numericals = data[numericals_columns]

for i in numericals_columns:
    # convertin No info s to None which will be handled by imputer
    numericals[i] = pd.to_numeric(numericals[i], errors='coerce')

imputer_numerical = SimpleImputer(missing_values=np.nan, strategy="mean")
normalized_numericals = (numericals - numericals.mean()) / numericals.std()
normalized_numericals = imputer_numerical.fit_transform(normalized_numericals)

#/////////////////////////////////////////////////////////////

#//////////////////// BINARY /////////////////////////////////
# actually not really binary

# # dont have enough time
# binary_columns = ["Focus on consumer data?", "Focus on private or public data?", "Presence of a top angel or venture fund in previous round of investment", "Worked in top companies", "Have been part of startups in the past?", "Have been part of successful startups in the past?", "Was he or she partner in Big 5 consulting?", "Consulting experience?", "Focus on private or public data?", "Focus on consumer data?", "Focus on structured or unstructured data", "Subscription based business", "Cloud or platform based serive/product?",
#                   "Local or global player", "Linear or Non-linear business model", "Crowdsourcing based business", "Crowdfunding based business", "Machine Learning based business", "Predictive Analytics business", "Speech analytics business", "Prescriptive analytics business", "Big Data Business", "Cross-Channel Analytics/ marketing channels", "Owns data or not? (monetization of data) e.g. Factual", "Is the company an aggregator/market place? e.g. Bluekai",  "B2C or B2B venture?"]


# binary = data[binary_columns]

# for i in binary_columns:
#     print(binary[i].iloc[:, 1])
#     binary[i] = le.fit_transform(binary[i].iloc[:, 1])
# print(binary)

#///////////////////////////////////////////
remaining_columns = [x for x in data.columns if x not in numericals_columns]


imputer = SimpleImputer(missing_values=np.nan, strategy="median")
remaining_data = pd.get_dummies(data[remaining_columns])

data_new = pd.concat(
    [remaining_data, pd.DataFrame(normalized_numericals)], axis=1)
data_processed = imputer.fit_transform(data_new)
data_processed = pd.DataFrame(data_new)


model = ExtraTreesClassifier()
model.fit(data_processed, labels)


feat_importances = pd.Series(
    model.feature_importances_, index=data_processed.columns)
print("not dead 5")
plt.figure(figsize=(14, 12))
feat_importances.nlargest(25).plot(kind='barh')
print("not dead 6")
plt.savefig("largest.png")
plt.show()
print('donene')
