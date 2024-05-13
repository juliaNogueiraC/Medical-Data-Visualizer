import unittest
from medical_data_visualizer import *

class TestDataVisualizer(unittest.TestCase):
    def setUp(self):
        # Carregar os dados para teste
        self.df = pd.read_csv('medical_examination.csv')

    def test_calculate_overweight(self):
        # Testar se a função calculate_overweight está funcionando corretamente
        df_with_overweight = calculate_overweight(self.df)
        self.assertTrue('overweight' in df_with_overweight.columns)  # Verificar se a coluna 'overweight' foi adicionada

    def test_normalize_data(self):
        # Testar se a função normalize_data está funcionando corretamente
        df_normalized = normalize_data(self.df)
        self.assertEqual(df_normalized['cholesterol'].max(), 1)  # Verificar se o colesterol máximo é 1
        self.assertEqual(df_normalized['gluc'].max(), 1)         # Verificar se a glicose máxima é 1

    def test_clean_data(self):
        # Testar se a função clean_data está funcionando corretamente
        df_cleaned = clean_data(self.df)
        self.assertTrue((df_cleaned['ap_lo'] <= df_cleaned['ap_hi']).all())  # Verificar se ap_lo <= ap_hi
        self.assertTrue((df_cleaned['height'] >= df_cleaned['height'].quantile(0.025)).all())  # Verificar altura >= 2.5th percentile
        self.assertTrue((df_cleaned['height'] <= df_cleaned['height'].quantile(0.975)).all())  # Verificar altura <= 97.5th percentile
        self.assertTrue((df_cleaned['weight'] >= df_cleaned['weight'].quantile(0.025)).all())  # Verificar peso >= 2.5th percentile
        self.assertTrue((df_cleaned['weight'] <= df_cleaned['weight'].quantile(0.975)).all())  # Verificar peso <= 97.5th percentile

    def test_draw_heat_map(self):
        # Testar se a função draw_heat_map está funcionando corretamente
        fig = draw_heat_map(self.df)
        self.assertIsNotNone(fig)  # Verificar se a figura foi gerada com sucesso

if __name__ == '__main__':
    unittest.main()
