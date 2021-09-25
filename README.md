# glfw-glew-build

`glfw` と `glew` を以下のターゲット向けに生成します。

- Windows: `x86`, `x64`
- Linux: 対象外
- Android: 対象外

## ビルド

`glfw` のソース一式を以下からダウンロードします。

- <https://github.com/glfw/glfw/releases/tag/3.3.4>

`glew` のソース一式を以下からダウンロードします。

- <https://github.com/nigels-com/glew/releases/tag/glew-2.1.0>

### Windows

```bash
$ python build_window.py
```

`glfw` のReleaseビルドで以下のようなリンクエラーになってしまう。

```text
glew.obj : error LNK2019: 未解決の外部シンボル memset が関数 glewContextInit で参照されました [C:\workspace\glfw-glew-build\glew-2.1.0\build
_win\glew.vcxproj]
C:\workspace\glfw-glew-build\glew-2.1.0\build_win\bin\Release\glew32.dll : fatal error LNK1120: 1 件の未解決の外部参照 [C:\worksp
ace\glfw-glew-build\glew-2.1.0\build_win\glew.vcxproj]
```

`build/cmake/CMakeLists.txt` の以下をコメントアウトしたら通ったが、果たしていいのかどうか分からない。

```cmake
  # remove stdlib dependency
  target_link_libraries (glew LINK_PRIVATE -nodefaultlib -noentry)
  string(REGEX REPLACE "/RTC(su|[1su])" "" CMAKE_C_FLAGS_DEBUG ${CMAKE_C_FLAGS_DEBUG})
```

### Linux

対象外

### Android

対象外
