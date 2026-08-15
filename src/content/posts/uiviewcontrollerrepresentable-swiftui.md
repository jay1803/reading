---
title: "利用 UIViewControllerRepresentable 協定在 SwiftUI 存取相簿並使用相機"
date: 2022-07-20T13:16:39Z
category: swift
description: "要將 UIImagePickerController 整合到 SwiftUI 專案中，我們可以使用 UIViewControllerRepresentable 協定"
source: "https://www.appcoda.com.tw/swiftui-camera-photo-library/"
---

## 使用 UIViewControllerRepresentable
要將 UIImagePickerController 整合到 SwiftUI 專案中，我們可以使用 UIViewControllerRepresentable 協定
```
struct ImagePicker: UIViewControllerRepresentable {
    func makeUIViewController(context: UIViewControllerRepresentableContext<ImagePicker>) -> UIImagePickerController {

        // Return an instance of UIImagePickerController
    }

    func updateUIViewController(_ uiViewController: UIImagePickerController, context: UIViewControllerRepresentableContext<ImagePicker>) {

    }
}
```

當初始化 ImagePicker 時，就會調用 makeUIViewController 方法。在該方法中，你需要實例化 (instantiate) UIImagePickerController，並配置其初始狀態。
## 在 SwiftUI 中創建 ImagePicker
```
struct ImagePicker: UIViewControllerRepresentable {

    var sourceType: UIImagePickerController.SourceType = .photoLibrary

    func makeUIViewController(context: UIViewControllerRepresentableContext<ImagePicker>) -> UIImagePickerController {

        let imagePicker = UIImagePickerController()
        imagePicker.allowsEditing = false
        imagePicker.sourceType = sourceType

        return imagePicker
    }

    func updateUIViewController(_ uiViewController: UIImagePickerController, context: UIViewControllerRepresentableContext<ImagePicker>) {

    }
}
```

## 使用 ImagePicker 在 SwiftUI 視圖中加載相簿
## 讓 Coordinator 採用 UIImagePickerControllerDelegate 協定
必須採用兩個委託 (delegate)：UIImagePickerControllerDelegate 和 UINavigationControllerDelegate，以便與 UIImagePickerController 進行交互。
