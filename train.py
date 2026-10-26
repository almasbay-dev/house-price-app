from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib

# 1. Данные
data = fetch_california_housing(as_frame=True)
X, y = data.data, data.target

# 2. Делим: 80% учим, 20% проверяем на невиданных данных
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Обучение
model = RandomForestRegressor(n_estimators=100, max_depth=12,
                              random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

# 4. Оценка качества
mae = mean_absolute_error(y_test, model.predict(X_test))
print(f"Средняя ошибка: {mae * 100_000:.0f} $")

# 5. Сохраняем модель в файл
joblib.dump(model, "model.joblib")