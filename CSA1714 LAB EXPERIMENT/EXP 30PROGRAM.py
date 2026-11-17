from sklearn.linear_model import LinearRegression

X = [[1], [2], [3], [4], [5], [6]]
y = [35, 40, 50, 55, 65, 70]

model = LinearRegression()

model.fit(X, y)

hours = [[7]]
result = model.predict(hours)

print("Predicted Marks:", round(result[0], 2))
