---
title: "现代图片选择器（PHPicker）在 SwiftUI 应用"
date: 2022-07-04T12:37:32Z
category: swift
description: "struct PhotoPicker: UIViewControllerRepresentable {"
source: "https://blog.csdn.net/qq_45513182/article/details/120582682"
---

### 2. 代码
#### 2.1 PhotoPicker 图库选取器的编写
```
struct PhotoPicker: UIViewControllerRepresentable {
    // 对 PHPickerViewController 的配置
    let configuration: PHPickerConfiguration
    // 获取输出结果，即选择的图片
    @Binding var pickerResult: [UIImage]
    // 是否展示图片选择器
    @Binding var isPresented: Bool
    // 后两个变量前的修饰符 @Binding，代表这两个变量与外部的变量绑定，由 SwiftUI 管理

    // 第一个方法是绘制 UIViewController 组件，这里我们要绘制一个 PHPickerViewController，所以返回值是这个组件
    func makeUIViewController(context: Context) -> PHPickerViewController {
        let controller = PHPickerViewController(configuration: configuration)
        controller.delegate = context.coordinator
        return controller.
    }

    // 第二个方法是更新 UIViewController 组件，这里我们不需要更新组件，就将方法体空着就好。
    func updateUIViewController(_ uiViewController: PHPickerViewController, context: Context) { }

    func makeCoordinator() -> Coordinator {
        Coordinator(self)
    }

    /**
     makeCoordinator 方法，创建一个协调器，并绑定调用的父类对象。这里要将协调的父类设为这个结构体（PhotoPicker）,所以要写为 Coordinator(self)。
     然后我们要定义一个 Coordinator 类，这个类要负责和 ViewController 与其他 SwiftUI 协调。在委托模式中，这个类当然要设置为 PHPickerViewControllerDelegate。
    */
    class Coordinator: PHPickerViewControllerDelegate {

        // 变量 parent，负责指定委托的父对象，这里的父对象是结构体 PhotoPicker，所以我们这样定义变量并且在初始化类时必须要传入一个有效的 PhotoPicker 对象。
        private let parent: PhotoPicker

        init(_ parent: PhotoPicker) {
            self.parent = parent
        }

        /**
        实现 picker 方法去定义当用户在选择器在选择好以后或者点击取消（dismiss）后要执行的动作。
        当点击成功或者取消时，都会返回一个 results，我们每次都需要处理这个 results，这里我们处理结果，并将结果中可读取的对象添加到 pickerResult 中。
        */
        func picker(_ picker: PHPickerViewController, didFinishPicking results: [PHPickerResult]) {
            for image in results {
                if image.itemProvider.canLoadObject(ofClass: UIImage.self) {
                    image.itemProvider.loadObject(ofClass: UIImage.self) {
                        (newImage, error) in
                        if let error = error {
                            print(error.localizedDescription)
                        } else {
                            self.parent.pickerResult.append(newImage as! UIImage)
                        }
                    }
                } else {
                    print("Loaded Asset is not a Image")
                }
            }
            parent.isPresented = false
        }
    }
}
```

SwiftUI 中集合 UIKit 功能的方法，就是在实现结构体时要实现 UIViewControllerRepresentable 协议

PHPickerViewControllerDelegate 的文档，要实现 picker 方法去定义当用户在选择器在选择好以后或者点击取消（dismiss）后要执行的动作。
