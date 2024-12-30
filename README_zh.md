# Markdown 筆記圖片上傳至 Imgur 工具

**其他語言: [[English](README.md) | [繁體中文](README_zh.md)]**

當將 HackMD 筆記或本地 Markdown 檔案上傳至 GitHub 時，圖片連結經常會失效，導致圖片無法顯示。此腳本能自動將圖片上傳至 Imgur，並替換 Markdown 檔案中的圖片連結。

## 前置作業

1. **設定環境變數**
   - 在專案目錄下建立 `.env` 檔案。
   - 新增以下內容：
     ```env
     # 無相簿模式
     CLIENT_ID=your_client_id
     CLIENT_SECRET=your_client_secret

     # 有相簿模式
     ALBUM_ID=your_album_id
     ACCESS_TOKEN=your_access_token
     ```

2. **設定筆記路徑**
   - 在專案目錄下建立或更新 `config.ini` 檔案。
   - 新增以下內容：
     ```ini
     [Paths]
     note_path=你的 Markdown 檔案路徑
     ```

## 使用方式

1. **修改 HackMD 筆記權限**（若適用）
   - 將 HackMD 筆記的「閱讀」權限暫時設為「所有人」，讓腳本能存取圖片。腳本執行完畢後，可以將權限改回「私人」。

2. **執行腳本**
   - 若要將圖片上傳至相簿，使用以下指令：
     ```bash
     python update_imgur_ALBUM.py
     ```
   - 若要不使用相簿上傳圖片，使用以下指令：
     ```bash
     python update_imgur_wo_album.py
     ```

3. （可選） **更新權限**
   - 若在步驟 1 中修改了 HackMD 筆記的「閱讀」權限，可將其改回「私人」。

4. **將筆記推送至 GitHub**
   - 將更新後的 Markdown 檔案提交並推送至 GitHub。

## 注意事項

- 此腳本會自動搜尋並替換 Markdown 檔案中 `i.imgur.com` 或 `hackmd.io` 的圖片連結，改為新的 Imgur 連結。
- 確保 `.env` 檔案中包含有效的 Imgur 憑證，並確認 Access Token 擁有足夠的圖片上傳權限。

## 範例設定

### 範例 `.env`
```env
CLIENT_ID=abc123
CLIENT_SECRET=xyz789
ALBUM_ID=your_album_id
ACCESS_TOKEN=your_access_token
```

### 範例 `config.ini`
```ini
[Paths]
note_path=/path/to/your/note.md
```

## 疑難排解

- **環境變數缺失：** 確保 `.env` 中已設定所有必要的變數。
- **筆記路徑錯誤：** 確認 `config.ini` 中的 `note_path` 指向正確的 Markdown 檔案。
- **Imgur 上傳失敗：** 檢查你的 Imgur 憑證，並確認 Access Token 有效。

透過此腳本，您可以輕鬆將圖片上傳至 Imgur，確保 Markdown 筆記在 GitHub 上依然完整，並且不需要長期公開 hackmd 筆記確保隱私。
