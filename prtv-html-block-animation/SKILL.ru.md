---
name: prtv-html-block-animation
description: Как оживить слайд цифровой вывески PRTV через HTML-блок — CSS keyframes, SVG-фильтры и SMIL, без JavaScript. Применять, когда ИИ-агенту или пользователю нужен пар, блик, ветер, ТВ-рябь, транспарант за самолётом или любой зацикленный эффект на слайде в конструкторе prtv.pro, а также когда нужно анимировать родной текст редактора, не превращая его в HTML.
license: CC-BY-4.0
metadata:
  product: Конструктор цифровых вывесок PRTV (prtv.pro)
  version: "1.0"
  date: "2026-09-06"
  language: ru
  scope: интерфейс редактора + чтение состояния страницы из DOM; без вызовов внутреннего API
---

# HTML-блок и анимация в конструкторе PRTV

Конструктор PRTV собирает слайд из элементов: текст, картинка, видео, фигуры, виджеты («информеры») и **HTML-блок**. HTML-блок — единственный элемент, в котором работает **произвольная** бесконечная анимация. Пресеты анимации в панели элемента тоже зацикливаются, если поставить количество повторов 0 (пульсирующий бейдж, мигающий акцент — см. prtv-element-layout), но это готовые формы; всё своё — блик по тексту, пар, ветер, транспарант за самолётом — это HTML-блок.

## Что HTML-блок умеет, а что нет

| | Правило |
|---|---|
| НЕТ | `<script>` вырезается. Ни canvas, ни случайных частиц, ни реакции на данные. Всё описывается заранее в CSS и SVG. |
| НЕТ | Атрибут `class` у `<img>` перезаписывается служебными классами редактора. Стилизовать картинки через селектор родителя: `.wrap img { … }`. |
| ДА | SVG-фильтры и **SMIL** (`<animate>`) работают — так делаются живой шум и колыхание ткани. |
| ДА | `<style>` внутри блока **глобален для документа** — из него можно целиться в родные элементы слайда. |
| ДА | Картинки из медиатеки PRTV использовать можно; URL берётся из `<img>`, уже стоящего на слайде. |

Содержимое обрезается по границам блока. Фон блока по умолчанию белый — гасить альфой (см. ниже).

**Тяжёлые пиксельные фильтры — только на малой площади.** Турбулентность и размытие считаются для каждого пикселя: квадрат 445×370 приставка тянет, полный кадр 1920×1080 — нет. На весь экран годятся только `transform` и `opacity` — их считает видеокарта.

## Создание блока

1. Кнопка **HTML** в тулбаре → блок 400×200 появляется в точке (0, 0).
2. Кликнуть по блоку, дождаться в панели элемента textarea **«Код HTML»**.
3. Вставить код. Набор с клавиатуры работает; длинный код надёжнее записать через нативный сеттер, чтобы редактор увидел изменение в своём состоянии:

```js
window.__setRV = function (el, val) {
  const proto = el.tagName === 'TEXTAREA' ? HTMLTextAreaElement.prototype : HTMLInputElement.prototype;
  Object.getOwnPropertyDescriptor(proto, 'value').set.call(el, val);
  el.dispatchEvent(new Event('input', { bubbles: true }));
  el.dispatchEvent(new Event('change', { bubbles: true }));
};
```

4. Фон элемента → пикер цвета → поле **A** (альфа) = 0. Сохранённое значение — `#ffffff00`.
5. Ресайз за маркеры рамки (самый надёжный — средний правый: нижние могут оказаться за краем экрана).
6. Перенос — драгом за **невыделенный** блок (сначала Escape). Драг по выделенному текстовому элементу открывает правку текста.
7. Выставить **Глубину** (z-index) — см. «Слои».

Проверять — перезагрузкой страницы. Сохраняется только реальный ввод: мышь, клавиатура, команды тулбара, запись через нативный сеттер. **Правки, внесённые скриптом прямо в DOM, не сохраняются** — редактор перерисовывает элемент из своего состояния, и после перезагрузки правка исчезает. Истории версий нет; undo живёт только в пределах сессии страницы.

## Слои

Глубина = z-index. Рабочая раскладка:

| Глубина | Слой |
|---|---|
| 0 | фоновая картинка или видео |
| 1 | атмосферные блоки: ветер, небо |
| 2–10 | родные тексты и картинки макета |
| 11–16 | перекрывающие блоки: плашка, рябь |
| 20 | текст поверх плашки |

Фон рисуется на глубине 0 и сам ничего не прячет. **Чтобы объект «выезжал из-под» детали фона, эту деталь надо перекрыть непрозрачной плашкой с глубиной выше анимации.**

## Время

В настройках слайда лежит **длительность показа**. Период анимаций подгонять под неё, чтобы цикл не обрывался посередине.

## Бегущая строка (родной элемент)

Панель: текст, скорость, направление, размер шрифта, шрифт, цвет текста, цвет фона, анимация, глубина. Механика — CSS-анимация на внутреннем span: translateX(ширина блока) → translateX(−ширина текста), linear infinite. **Скорость × 10 = px/с** (20 → 200 px/с); длительность подстраивается под длину текста.

Следствие: жёстко синхронизировать бегущую строку с отдельно анимированной картинкой нельзя — правка текста меняет период. Для связки «самолёт и транспарант» класть картинку и текст **в один HTML-блок с одной анимацией**.

## Анимация родного текста без превращения в HTML

Контент родного текста — HTML со span, у которых инлайновые стили. Поскольку style из HTML-блока глобален, родной спан можно поймать по одному из инлайновых свойств, например по размеру шрифта:

```css
.text-widget span[style*="font-size: 52px"] {
  display: inline-block;
  background: linear-gradient(100deg, #C9A24B 0 40%, #FFF0C8 50%, #C9A24B 60% 100%);
  background-size: 280% 100%;
  -webkit-background-clip: text; background-clip: text;
  color: transparent !important; -webkit-text-fill-color: transparent;
  animation: promoShine 5s linear infinite;
}
@keyframes promoShine { from { background-position: 190% 0 } to { background-position: -90% 0 } }
```

Текст остаётся редактируемым; правка слов блик не ломает.

## Проверка анимации

Скриншот не передаёт движение. Ровные кадры снимаются перемоткой:

```js
const a = el.getAnimations()[0];
a.pause(); a.currentTime = 4000; // мс
// снять кадр
a.play();
```

Кадры сохранить, склеить в GIF, показать результат.

## Рецепты

### Транспарант за самолётом

Картинка и текст в одном flex-ряду с общей анимацией — синхронизация гарантирована при любом тексте.

```html
<div class="tow">
  <img src="URL_КАРТИНКИ" alt="">
  <span class="rope"></span>
  <div class="cloth"><span class="cloth-t">ТЕКСТ АКЦИИ</span></div>
</div>
<svg width="0" height="0">
  <filter id="towWind" x="-15%" y="-60%" width="130%" height="220%">
    <feTurbulence type="fractalNoise" baseFrequency="0.006 0.018" numOctaves="2" seed="7" result="noise">
      <animate attributeName="baseFrequency" dur="6s" values="0.006 0.018;0.012 0.030;0.006 0.018" repeatCount="indefinite"/>
    </feTurbulence>
    <feDisplacementMap in="SourceGraphic" in2="noise" scale="7" xChannelSelector="R" yChannelSelector="G"/>
  </filter>
</svg>
<style>
.tow{position:relative;height:145px;display:flex;align-items:center;white-space:nowrap;will-change:transform;animation:towFly 16s linear infinite}
.tow img{width:218px;height:101px;flex:none;object-fit:contain;margin:0}
.rope{flex:none;width:44px;height:3px;background:#2a241c;opacity:.5;margin:0 6px}
.cloth{font-family:Oswald,sans-serif;font-size:40px;letter-spacing:3px;color:#2a241c;line-height:1;filter:url(#towWind);animation:towFlap 3.2s ease-in-out infinite;transform-origin:left center}
@keyframes towFly{0%{transform:translateX(1500px)}78%{transform:translateX(-820px)}100%{transform:translateX(-820px)}}
@keyframes towFlap{0%,100%{transform:skewY(-1.6deg) rotate(-.5deg)}50%{transform:skewY(1.6deg) rotate(.5deg)}}
</style>
```

Расчёт цикла: стартовый translateX — положение, при котором связка целиком спрятана за перекрывающей плашкой; финиш ≤ минус ширина связки; хвост цикла — пауза, чтобы перезапуск не был виден. filter: url(#…) на тексте даёт колыхание ткани — «волна на ветру» без JS.

### ТВ-рябь

```html
<div class="tvfx">
  <svg class="tvfx-n" preserveAspectRatio="none" viewBox="0 0 320 265">
    <defs>
      <filter id="tvfxNoise" x="0" y="0" width="100%" height="100%">
        <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="2" stitchTiles="stitch">
          <animate attributeName="seed" values="1;4;7;11;15;19;23;27" dur="0.42s" calcMode="discrete" repeatCount="indefinite"/>
        </feTurbulence>
        <feColorMatrix type="saturate" values="0"/>
      </filter>
    </defs>
    <rect width="320" height="265" filter="url(#tvfxNoise)" opacity="0.17"/>
  </svg>
  <div class="tvfx-scan"></div>
  <div class="tvfx-roll"></div>
</div>
<style>
.tvfx{position:relative;width:100%;height:100%;overflow:hidden;pointer-events:none}
.tvfx-n{position:absolute;inset:0;width:100%;height:100%;mix-blend-mode:screen}
.tvfx-scan{position:absolute;inset:0;background:repeating-linear-gradient(to bottom,rgba(255,255,255,.055) 0 2px,transparent 2px 6px)}
.tvfx-roll{position:absolute;left:0;right:0;height:20%;background:linear-gradient(to bottom,transparent,rgba(255,255,255,.07),transparent);animation:tvfxRoll 7s linear infinite}
@keyframes tvfxRoll{from{transform:translateY(-140%)}to{transform:translateY(560%)}}
</style>
```

Держать на малой площади («экран» внутри макета), не на всём кадре.

### Ветер: порывы и лепесток

```html
<div class="wind">
  <i class="g" style="top:12%;width:24%;animation-duration:11s"></i>
  <i class="g" style="top:63%;width:28%;animation-duration:12.5s;animation-delay:1.5s;opacity:.8"></i>
  <i class="p" style="top:8%;animation-duration:22s;animation-delay:1s"></i>
</div>
<style>
.wind{position:relative;width:100%;height:100%;overflow:hidden;pointer-events:none}
.wind i{position:absolute;display:block;left:-26%;will-change:transform}
.wind .g{height:3px;border-radius:3px;background:linear-gradient(to right,rgba(120,110,95,0),rgba(120,110,95,.4),rgba(120,110,95,0));animation:windGust linear infinite}
@keyframes windGust{from{transform:translateX(0)}to{transform:translateX(1960px)}}
.wind .p{width:15px;height:18px;background:linear-gradient(135deg,#fff,#D6CFC1);clip-path:polygon(0 12%,100% 0,86% 100%,10% 84%);filter:drop-shadow(0 2px 3px rgba(0,0,0,.18));animation:windFleck linear infinite}
@keyframes windFleck{0%{transform:translate(0,0) rotate(0)}50%{transform:translate(980px,-46px) rotate(200deg)}100%{transform:translate(1960px,28px) rotate(400deg)}}
</style>
```

Ширину блока обрезать так, чтобы лепестки не пролетали поверх плотных карточек.

### Парение и покачивание на месте

```css
@keyframes skyFloat{0%{transform:translate(0,0) rotate(-1.5deg)}50%{transform:translate(6px,-16px) rotate(1.5deg)}100%{transform:translate(0,0) rotate(-1.5deg)}}
@keyframes skySail{0%{transform:translate(0,0)}25%{transform:translate(-75px,-8px) rotate(-.8deg)}50%{transform:translate(-150px,0)}75%{transform:translate(-75px,8px) rotate(.8deg)}100%{transform:translate(0,0)}}
```

Несколько декоративных картинок удобнее держать в **одном** блоке-«небе» с абсолютным позиционированием внутри, а не отдельными родными элементами.

## Чего не делать

- Не вешать пиксельные фильтры (турбулентность, размытие) на весь кадр.
- Не считать правку через DOM сохранённой без перезагрузки.
- Не пытаться собрать свой эффект из пресетов панели элемента — с повтором 0 они зацикливаются, но только как есть.
- Не кликать вслепую сериями двойных кликов: лишний клик уносит элемент драгом за пределы слайда.
- Не кликать «на всякий случай» рядом с полосой миниатюр — там всплывают кнопки, включая удаление слайда.

## Связанные скиллы

prtv-editor-overview · prtv-text-element · prtv-element-layout · prtv-agent-rules