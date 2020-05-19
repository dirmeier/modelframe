
import numpy as np
import pandas as pd

from modelframe import model_frame

if __name__ == '__main__':
    df = pd.read_csv(
        "https://raw.githubusercontent.com/dirmeier/mixed-models/master/data/sleepstudy.csv"
    )
    df = df.head()
    df.Subject = np.array([308, 308, 309, 309, 310])
    df["Subject"] = df["Subject"].astype("category")
    model_frame("~ Reaction + (Days | Subject)", df)
    # print("-------")
    # model_frame("~ X +  Y", df)
    # print("-------")
    # model_frame("~ 1 | Days", df)
    # print("-------")
    # model_frame("~ (1 | Days) + X", df)

