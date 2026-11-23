/* Zekacademy kitapları: konu PDF'i indirme anında öğrencinin adı ve numarasıyla damgalanır (paylaşılmasın diye).
   PDF'ler Storage'da kitaplar/<kod>/<dosya>; öğrenci depoya doğrudan erişemez, yalnız bu fonksiyon okur. */
import { readFileSync } from "node:fs";
import { PDFDocument, rgb, degrees } from "pdf-lib";
import fontkit from "@pdf-lib/fontkit";
const FONT = readFileSync(new URL("./kitap/Poppins-Medium.ttf", import.meta.url));
const MM = 72 / 25.4;
export const KITAP_KODLAR = ["tyt-mat", "tyt-fiz", "tyt-kim", "tyt-bio"];
export const dosyaGecerli = (kod, dosya) => KITAP_KODLAR.includes(kod) && /^[0-9]{2}-[A-Za-z0-9-]+\.pdf$/.test(dosya || "");
export async function damgala(pdfBytes, ad, no) {
  const doc = await PDFDocument.load(pdfBytes);
  doc.registerFontkit(fontkit);
  const font = await doc.embedFont(FONT, { subset: true });
  const tarih = new Date().toLocaleDateString("tr-TR", { timeZone: "Europe/Istanbul" });
  const alt = `${ad} · #${no} için hazırlanmıştır · ${tarih} · paylaşılamaz`, yan = `${ad} · #${no} · Zekacademy`, renk = rgb(0.45, 0.48, 0.47);
  doc.getPages().forEach((p, i) => {
    const { width, height } = p.getSize();
    p.drawText(alt, { x: (width - font.widthOfTextAtSize(alt, 6.2)) / 2, y: 4.2 * MM, size: 6.2, font, color: renk, opacity: 0.9 });
    if (i > 0) p.drawText(yan, { x: width - 6 * MM, y: height / 2 - font.widthOfTextAtSize(yan, 6) / 2, size: 6, font, color: renk, opacity: 0.55, rotate: degrees(90) });
  });
  doc.setAuthor(`Zekacademy — ${ad} (#${no})`); doc.setKeywords([`ogrenci:${no}`]);
  return doc.save({ useObjectStreams: true });
}
