import pandas as pd


class DemandClass(object):
    def __init__(self, customer, product, demand_quantity, period, demand_type, Channel):
        self.customer = customer
        self.product = product
        self.demand_quantity = demand_quantity
        self.period = period
        self.type = demand_type
        self.channel = Channel

    def __repr__(self):
        pass

    def __str__(self):
        return "this object is : demand of customer {0} " \
               "for product {1} " \
               "at time {2} " \
               "of type {3} " \
               "in channel {4}".format(self.customer, self.product, self.period, self.type, self.channel)

    def __lt__(self, other):
        # return self.demand_quantity < other.demand_quantity
        return self.period > other.period

    def distance(self, other):
        """

        if self.type == other.type:
            return 0
        else:
            return 1
        """
        return abs(self.demand_quantity - other.demand_quantity)


# reading demand table
_df = pd.read_csv('./demand.csv')

"""
# First way
demand_objects_list = []
demand_objects_dict = {}
for index, row in _df.iterrows():
    print()
    demand_object = DemandClass(customer=row["customer"], product=row["product"],
                                demand_quantity=row["demand_quantity"],
                                period=row["period"], demand_type=row["demand_type"],
                                Channel=row["Channel"])
    demand_objects_list.append(demand_object)
    demand_objects_dict[(row["customer"], row["product"], row["period"])] = demand_object
    print()
"""

"""
# Second Way
_df['demand_object'] = _df.apply(lambda row: DemandClass(customer=row["customer"], product=row["product"],
                                                         demand_quantity=row["demand_quantity"],
                                                         period=row["period"], demand_type=row["demand_type"],
                                                         Channel=row["Channel"]),
                                 axis=1)
"""

_df['demand_object'] = _df.apply(lambda row: DemandClass(**row), axis=1)

print(_df['demand_object'].iloc[0])
s = str(_df['demand_object'].iloc[0])

x = "stop to take a look at _df"

demand_object_in_row_3 = _df['demand_object'].iloc[2]
d = demand_object_in_row_3.demand_quantity
x = "Lets look at demand object in row 3"

# A pandas series with (customer, product, period)s as keys and demand_objects as values
demand_series = _df.set_index(["customer", "product", "period"])["demand_object"]
demand_series.sort_index(inplace=True)

# demand object for customer c1 for product p2 in period 3
d = demand_series["c1", "p1", 3].demand_quantity
x = "Lets take a look at d"

# Channel series
channel_series = demand_series.apply(lambda item: item.channel)
print("Here is the channel's order frequency: ")
print(channel_series.value_counts())

d1 = demand_series["c1", "p1", 3]
d2 = demand_series["c1", "p1", 2]

print("the distance is :", d1.distance(d2))
