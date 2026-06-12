# 🚀 Git & Cmder Quick Reference Guide

هذا الدليل يحتوي على جميع الأوامر الأساسية المستخدمة لإدارة المستودع (Repository) عبر الـ Cmder/Terminal، سواء للرفع لأول مرة، التحديث، أو حذف الملفات.

---

## 📂 1. الرفع لأول مرة (Initial Setup & Push)
*تُستخدم هذه الأوامر عندما تقوم بإنشاء مشروع جديد تماماً على جهازك وتريد ربطه ومزامنته مع موقع GitHub لأول مرة.*

```bash
# 1. الدخول إلى القرص D (إذا كان مشروعك هناك)
D:

# 2. الدخول إلى مجلد المشروع الرئيسي
cd "D:\Path\To\Your\AWS-Folder"

# 3. تهيئة مستودع جيت محلي جديد في الفولدر
git init

# 4. تجهيز جميع الملفات والفولدرات داخل المجلد للرفع
git add .

# 5. تثبيت الملفات وإعطاء رسالة توضيحية للرفع
git commit -m "Initial commit: Add project structure"

# 6. ربط المجلد المحلي بمستودع جيت هاب (ضع الرابط الخاص بك)
git remote add origin [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)

# 7. تسمية الفرع الرئيسي بـ main
git branch -M main

# 8. دفع الملفات أونلاين إلى جيت هاب
git push -u origin main



# *للتعديل واضافة ملفات *
# 1. الدخول لمسار المشروع (تأكد دائماً أنك في المسار الصحيح)
cd /d "D:\Path\To\Your\AWS-Folder"

# 2. جعل جيت يقرأ جميع الإضافات والتعديلات الجديدة
git add .

# 3. حفظ التعديل بكتابة رسالة تصف اللاب الجديد الذي أضفته
git commit -m "Add: Lab 04 EC2 Auto-Scaling with screenshots"

# 4. رفع التحديثات فوراً أونلاين لـ جيت هاب
git push origin main


# الخطوة الأولى: قم بحذف الملف أو الفولدر يدوياً من جهازك (كليك يمين ثم Delete)

# الخطوة الثانية: افتح Cmder واكتب الأوامر التالية ليلاحظ جيت عملية الحذف ويطبقها أونلاين:

# 1. جعل جيت يلاحظ حذف الملفات
git add .

# 2. تثبيت عملية الحذف برسالة توضيحية
git commit -m "Remove: Delete unwanted temporary files"

# 3. تحديث الموقع أونلاين ليختفي الملف من جيت هاب
git push origin main




#قم بإنشاء ملف نصي بسيط داخل الفولدر الرئيسي وسمّه بالظبط: .gitignore
add name of files you need to hide it
