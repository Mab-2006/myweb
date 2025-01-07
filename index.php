<?php
// در اینجا می‌توانیم متغیرها و داده‌ها را تنظیم کنیم که برای بخش‌های مختلف صفحه استفاده می‌شوند
$site_title = "Forex and Crypto Solutions";
$about_text = "We are a platform dedicated to providing the latest insights and tools for Forex and cryptocurrency trading. Our goal is to help both beginners and seasoned traders understand and navigate the dynamic world of financial markets.";
$forex_text = "Forex trading, also known as foreign exchange trading or currency trading, involves the exchange of currencies on the global market. It is one of the largest and most liquid financial markets in the world, with a daily turnover exceeding $6 trillion. Forex trading allows investors to profit from the fluctuations in currency prices, and it can be done 24 hours a day, 5 days a week.";
$crypto_text = "Cryptocurrency is a digital or virtual currency that uses cryptography for security. Unlike traditional currencies issued by governments, cryptocurrencies are decentralized and often built on blockchain technology. Bitcoin, Ethereum, and other cryptocurrencies have gained significant popularity as alternative investments and are widely traded on various crypto exchanges.";
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php echo $site_title; ?></title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../static/css/style.css"> <!-- لینک به فایل CSS جداگانه -->
</head>
<body>

    <!-- Upper Header (New Section) with buttons -->
    <div class="upper-header">
        <div class="logo">
            <img src="../static/images/logo.png" alt="Logo" width="50" height="50"> <!-- لوگو -->
            <h1><?php echo $site_title; ?></h1> <!-- عنوان سایت -->
        </div>
        <div class="auth-buttons">
            <button onclick="location.href='/login'">Login</button>
            <button onclick="location.href='/register'">Register</button>
        </div>
    </div>

    <!-- Main Header with Logo and Site Title -->
    <header>
        <div class="logo-menu">
            <!-- Navigation Links -->
            <nav>
                <a href="#">Home</a>
                <a href="#about">About Us</a>
                <a href="#forex">Forex</a>
                <a href="#crypto">Crypto</a>
                <a href="#contact">Contact</a>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <div class="hero-content">
            <h1>Welcome to Forex and Crypto Trading</h1>
            <p>Explore the World of Financial Markets with Forex and Cryptocurrency</p>
            <p style="font-size: 1.2rem; color: #ddd;">Scroll down to learn more about trading opportunities</p>
        </div>
    </section>

    <!-- About Us Section -->
    <section id="about">
        <h2>About Us</h2>
        <p><?php echo $about_text; ?></p>
    </section>

    <!-- Forex Trading Section -->
    <section id="forex">
        <h2>What is Forex Trading?</h2>
        <p><?php echo $forex_text; ?></p>
        <div class="ai-details">
            <h2>Why Trade Forex?</h2>
            <p>Forex offers high liquidity, flexibility, and a range of trading opportunities. Traders can take advantage of currency pair movements in both rising and falling markets. The ability to trade on margin allows for the potential of higher returns with a smaller initial investment. With the right strategy, Forex trading can be profitable for both short-term and long-term investors.</p>
        </div>
    </section>

    <!-- Cryptocurrency Section -->
    <section id="crypto">
        <h2>What is Cryptocurrency?</h2>
        <p><?php echo $crypto_text; ?></p>
        <div class="ai-details">
            <h2>Why Invest in Cryptocurrencies?</h2>
            <p>Cryptocurrencies offer the potential for high returns due to their volatility and emerging market status. Investors are attracted to the decentralized nature of crypto, as it provides more control over assets without relying on traditional banking systems. Additionally, many cryptocurrencies have a limited supply, which could drive up their value over time, making them a viable investment option for those willing to take risks.</p>
        </div>
    </section>

    <!-- Footer Section -->
    <div class="footer">
        <p>&copy; 2024 MohammadAmin Baranzehi. All Rights Reserved. | <a href="#">Privacy Policy</a></p>
    </div>

    <script src="../static/js/script.js"></script>
</body>
</html>
