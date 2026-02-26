import plotly.express as px
import pandas as pd

# -------------------------------
# Exercise 1
# -------------------------------

def survival_demographics():
    """Analyze Titanic survival patterns by class, sex, and age group."""

    df = pd.read_csv(
         "https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv"
    )

    # Create age categories
    bins = [0, 12, 19, 59, float("inf")]
    labels = ["Child", "Teen", "Adult", "Senior"]

    df["age_group"] = pd.cut(
         df["Age"],
         bins=bins,
         labels=labels
    )

    results = (
        df.groupby(["Pclass", "Sex", "age_group"], dropna=False)
        .agg(
            n_passengers=("Survived", "count"),
            n_survivors=("Survived", "sum")
       )
       .reset_index()
    )

    results["survival_rate"] = (
 results["n_survivors"] / results["n_passengers"]
)

    return results


def visualize_demographic():
  summary = survival_demographics()

  fig1 = px.bar(
    summary,
    x="age_group",
    y="survival_rate",
    color="Sex",
    facet_col="Pclass",
    barmode="group",
    title="Survival Rates by Class, Sex, and Age Group"
)

  return fig1


# -------------------------------
# Exercise 2
# -------------------------------

def family_groups():
     """Analyze family size, class, and fare patterns."""

     df = pd.read_csv(
    "https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv"
     )

     df["family_size"] = df["SibSp"] + df["Parch"] + 1
     
     grouped = (
         df.groupby(["Pclass", "family_size"])
         .agg(
             n_passengers=("PassengerId", "count"),
             avg_fare=("Fare", "mean"),
             min_fare=("Fare", "min"),
             max_fare=("Fare", "max")
         )
         .reset_index()
         .sort_values(["Pclass", "family_size"])
     )

     return grouped


def last_names():
    df = pd.read_csv(
        "https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv"
    )
    df["last_name"] = df["Name"].str.split(",").str[0]

    return df["last_name"].value_counts()


def visualize_families():
    summary = family_groups()
    
    fig2 = px.line(
        summary,
        x="family_size",
        y="avg_fare",
        color="Pclass",
        markers=True,
        title="Average Fare by Family Size and Passenger Class"
    )

    return fig2

