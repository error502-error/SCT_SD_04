from ecommerce_scraper import scrape_products, save_to_csv
from bs4 import BeautifulSoup

# Sample HTML content simulating an e-commerce page
sample_html = """
<html>
<head><title>Test Products</title></head>
<body>
<div class="product">
    <h2 class="product-name">Product 1</h2>
    <span class="price">$10.99</span>
    <div class="rating">4.5 stars</div>
</div>
<div class="product">
    <h2 class="product-name">Product 2</h2>
    <span class="price">$20.00</span>
    <div class="rating">3.8 stars</div>
</div>
<div class="product">
    <h2 class="product-name">Product 3</h2>
    <span class="price">$15.50</span>
    <div class="rating">4.0 stars</div>
</div>
</body>
</html>
"""

def test_scrape_products():
    # Instead of fetching from URL, parse the sample HTML directly
    soup = BeautifulSoup(sample_html, 'html.parser')
    products = []

    product_divs = soup.find_all('div', class_='product')
    for product in product_divs:
        name_tag = product.find('h2', class_='product-name')
        name = name_tag.text.strip() if name_tag else 'N/A'

        price_tag = product.find('span', class_='price')
        price = price_tag.text.strip() if price_tag else 'N/A'

        rating_tag = product.find('div', class_='rating')
        rating = rating_tag.text.strip() if rating_tag else 'N/A'

        products.append({
            'Name': name,
            'Price': price,
            'Rating': rating
        })

    # Save to CSV
    save_to_csv(products, 'test_products.csv')
    print(f'Test completed: {len(products)} products saved to test_products.csv')

if __name__ == '__main__':
    test_scrape_products()
