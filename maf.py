
# ملف تشغيل للوحدة المشفرة maf.cpython-311.so
import maf

# تأكد أن الدالة الرئيسية موجودة داخل الملف الأصلي
if hasattr(maf, 'main'):
    maf.main()
else:
    print("تم استيراد maf بنجاح، ولكن لا توجد دالة main للتشغيل.")
