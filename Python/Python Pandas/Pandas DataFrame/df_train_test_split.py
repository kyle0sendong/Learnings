from sklearn.model_selection import train_test_split    # splitting training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=1/3, random_state=random.randrange(0, 42))