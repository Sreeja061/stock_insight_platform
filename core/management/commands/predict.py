from django.core.management.base import BaseCommand
from core.utils import predict_stock

class Command(BaseCommand):
    help = 'Predict stock price for a given ticker symbol'

    def add_arguments(self, parser):
        parser.add_argument('--ticker', type=str, help='Stock ticker symbol (e.g. TSLA)')

    def handle(self, *args, **options):
        ticker = options['ticker']
        if not ticker:
            self.stdout.write(self.style.ERROR('Please provide a --ticker argument'))
            return

        result = predict_stock(ticker)
        self.stdout.write(self.style.SUCCESS(f"Predicted Price: {result['predicted_price']}"))
        self.stdout.write(f"Metrics: {result['metrics']}")
        self.stdout.write(f"Charts: {result['chart_1']}, {result['chart_2']}")
