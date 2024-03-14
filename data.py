from collections import defaultdict


class Data:
    @staticmethod
    def get_data(data_name, query):
        data = query
        data_counts = defaultdict(int)
        for data, count in data:
            data_counts[data] = count

        # Prepare data for Google Charts
        chart_data = [[f'{data_name.capitalize()}', 'Count']]  # Initialize with column headers
        for data_name, count in data_counts.items():
            chart_data.append([str(data_name), count])
        return chart_data


