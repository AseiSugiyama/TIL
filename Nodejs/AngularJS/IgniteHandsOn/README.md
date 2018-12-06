# Ignite Handson

[Angular で始めるモダン Web 開発セミナー](https://connpass.com/event/106227/?utm_campaign=event_message_to_selected_participant&utm_source=notifications&utm_medium=email&utm_content=title_link) で行った、ハンズオンの内容の一部です。

[はじめに - Ignite UI for Angular](https://jp.infragistics.com/products/ignite-ui-angular/getting-started) に従うと、同じ内容のアプリケーションができあがります。

ハンズオンではさらに踏み込んだ内容を行いました。こちらは公開されていないようなので、そこまでは実装しません。

## 変更点

Webページでの記述とは変更している箇所がありますので記します。

### 2-1. Angular CLIプロジェクトの作成

CSSのフォーマットの選択でSCSSを選択しました。[はじめに - Ignite UI for Angular](https://jp.infragistics.com/products/ignite-ui-angular/getting-started) はSCSSではなく、CSS選択前提になっているようです。

### 3-3. app.component.tsの編集

`app.component.ts` では `app.component.css` が存在しないので `ng serve -o` を実行すると次のエラーが表示されコンパイルに失敗します。エラーメッセージ中の`/Path/To/Your/App/`部分は実行している環境依存です。

```text
ERROR in ./src/app/app.component.ts
Module not found: Error: Can't resolve './app.component.css' in '/Path/To/Your/App/my-app/src/app'
```

これを解決するために、次の様に変更しています。

```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  // styleUrls: ['./app.component.css'] // Before
  styleUrls: ['./app.component.scss'] // After
})
export class AppComponent {
  title = '備品リスト';

  onClickMenu() {
    console.log('Menu Clicked');
  }
}

```

## Reference

### Event

* [Angular で始めるモダン Web 開発セミナー - connpass](https://connpass.com/event/106227/?utm_campaign=event_message_to_selected_participant&utm_source=notifications&utm_medium=email&utm_content=title_link)

### Angular

* [Angular](https://angular.io/)
* [Angular Update Guide](https://update.angular.io/)

### Ignite

* [Angular 対応コンポーネント Ignite UI for Angular](https://jp.infragistics.com/products/ignite-ui-angular)
* [はじめに - Ignite UI for Angular](https://jp.infragistics.com/products/ignite-ui-angular/getting-started#tab-npm)
