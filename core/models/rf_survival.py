from sklearn.ensemble import RandomForestClassifier
import numpy as np

class FirmExitPredictor:
    def __init__(self):
        # Initialize the Random Forest classifier
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.is_trained = False

    def train_dummy_model(self):
        """
        Trains the model on generated dummy data representing firm financials and KPIs.
        """
        # Features: [liquidity_ratio, debt_to_equity, employee_turnover, market_demand_trend]
        X_train = np.random.rand(100, 4) 
        # Labels: 0 (survives), 1 (exits/distressed)
        y_train = np.random.randint(0, 2, 100)
        
        self.model.fit(X_train, y_train)
        self.is_trained = True
        print("Random Forest model trained on dummy SMM data.")

    def predict_exit_probability(self, firm_features: list) -> float:
        if not self.is_trained:
            self.train_dummy_model()
            
        features_array = np.array(firm_features).reshape(1, -1)
        # Return the probability of class 1 (shutting down)
        exit_prob = self.model.predict_proba(features_array)[0][1]
        return float(exit_prob)