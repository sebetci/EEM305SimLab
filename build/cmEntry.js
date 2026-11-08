// CodeMirror paketini tek global nesne olarak dışa aktarır
export { EditorView, basicSetup } from "codemirror";
export { EditorState, Compartment } from "@codemirror/state";
export { keymap } from "@codemirror/view";
export { StreamLanguage, HighlightStyle, syntaxHighlighting } from "@codemirror/language";
export { linter, lintGutter, setDiagnostics } from "@codemirror/lint";
export { autocompletion } from "@codemirror/autocomplete";
export { indentWithTab } from "@codemirror/commands";
export { tags } from "@lezer/highlight";
