import pandas as pd
import yaml





class Helper:



    def __init__(self):
        self.config_path =  "config\\paths.yaml"

    def open_yaml(self):
        arquivo_yaml = self.config_path
        with open(arquivo_yaml, 'r') as arquivo:
            config = yaml.safe_load(arquivo)

        self.config = config
    
    def load_main_file(self):

        config = self.config

        players_path = config['players_path']


        df_data = pd.read_csv(players_path, index_col=0)
        df_data['Playing Time Min'] = int(df_data['Playing Time Min'])
        df_data = df_data[df_data['Playing Time Min'] >= 0]
        
        return df_data


