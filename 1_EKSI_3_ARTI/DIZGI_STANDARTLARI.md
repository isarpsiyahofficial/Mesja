# 1 Eksi 3 Artı - Dizgi Standartları

Bu standartlar kitabın ilk sayfasından son sayfasına kadar korunacaktır. Amaç, bölüm sayısı arttıkça yeniden biçimlendirme ihtiyacını ortadan kaldırmaktır.

## Sayfa

- Nihai kitap boyutu: **A5 - 148 x 210 mm**.
- Karşılıklı sayfalar kitap baskısı mantığıyla iç/dış marj kullanır.
- İç marj: 20 mm.
- Dış marj: 16 mm.
- Üst marj: 17 mm.
- Alt marj: 20 mm.
- Gövde metni sayfa sınırına taşmayacak; dip ve dış kenarlarda güvenli boşluk korunacak.

## Yazı karakteri

- Gövde: **Noto Serif**.
- Başlıklar: **Noto Sans**.
- Türkçe karakterlerin tamamı gömülü font ile üretilecek.
- Gövde boyutu: 10.7 pt.
- Satır yüksekliği: 1.48.
- Ana bölüm başlığı: 19 pt, yarı kalın/kalın.
- Ara başlık: 13.5 pt.

## Paragraf

- Gövde metni iki yana yaslıdır.
- Normal paragraflarda ilk satır girintisi: 5 mm.
- Bölüm başlığından, ara başlıktan veya sahne kırılmasından sonraki ilk paragraf girintisizdir.
- Normal paragraflar arasında yapay boşluk bırakılmaz.
- Diyalog ve kısa vurgu paragrafları doğal akışa göre korunur.
- Tek satırlık paragrafın sayfa başında/sonunda yalnız kalması mümkün olduğunca engellenir.
- Dul/yetim satır hedefi: en az 3 satır.

## Bölümler

- Yeni ana bölüm mümkün olduğunda sağ sayfadan başlar.
- Başlık ile ilk paragraf birbirinden koparılmaz.
- Bölüm başında gereksiz süs, ikon veya dekoratif çizgi kullanılmaz.
- Sahne kırılması gerekiyorsa ortalanmış `* * *` kullanılır.

## Sayfa numarası

- Kapak/başlık sayfasında görünmez.
- Ana metin başladığında alt dış kısımda sade biçimde görünür.
- Sayfa numarası gövde metninin içine girmez.

## Dil ve işaretler

- Türkçe tırnak ve noktalama tutarlılığı korunur.
- Üç nokta yerine gereksiz “...” yığınları kullanılmaz; metin gerektiriyorsa tek standart kullanılır.
- Yapay satır kırmalarıyla sayfa doldurulmaz.
- PDF'ye çalışma notu, editör notu, yapay zekâ notu veya planlama açıklaması girmez.

## PDF üretim kuralı

- Tek yetkili metin kaynağı: `KITAP_METNI.md`.
- `KITAP_HARITASI.md`, `DIZGI_STANDARTLARI.md` ve `DEGISIKLIK_GUNLUGU.md` kitap PDF'sine otomatik dahil edilmez.
- PDF her güncellemede aynı üretim betiği ve aynı CSS kurallarıyla yeniden oluşturulur.
- Her teslimden önce PDF sayfaları görsel olarak render edilip taşma, kesilme, bozuk Türkçe karakter, satır çakışması ve sayfa numarası hatası kontrol edilir.
