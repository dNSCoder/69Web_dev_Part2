from django.db import migrations

DEMO_TITLES = [
    "ซื้อของเข้าบ้าน",
    "ส่งการบ้านวิชา Web Programming",
    "ประชุมทีมโปรเจกต์",
    "อ่านเปเปอร์เรื่อง HTMX",
    "ออกกำลังกาย 30 นาที",
    "รีวิวโค้ด PR ของเพื่อน",
    "เตรียมสไลด์นำเสนอ",
    "จองตั๋วเดินทางกลับบ้าน",
    "แก้บั๊กหน้า login",
    "อัปเดตเอกสาร README",
    "โทรหาที่ปรึกษาโปรเจกต์",
    "แบ็คอัพฐานข้อมูล",
]


def seed_data(apps, schema_editor):
    DemoItem = apps.get_model("showcase", "DemoItem")
    for title in DEMO_TITLES:
        DemoItem.objects.get_or_create(title=title)


def unseed_data(apps, schema_editor):
    DemoItem = apps.get_model("showcase", "DemoItem")
    DemoItem.objects.filter(title__in=DEMO_TITLES).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("showcase", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_data, unseed_data),
    ]
