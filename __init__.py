"""A tool to run Text Editor scripts from a menu"""

import os
import bpy
import rna_keymap_ui
import re
import json

bl_info = {
    "name": "LK Script Runner",
    "description": "A tool to run Text Editor scripts from a menu",
    "author": "Ludvik Koutny",
    "version": (1, 0, 0),
    "blender": (3, 6, 0),
    "category": "Development"
}


def scripts_menu(self, _context):
    layout = self.layout
    for text in bpy.data.texts:
        if text.lines:
            first_line = text.lines[0].body
            if first_line == "import bpy":
                op = layout.operator("lk.script_runner_run_script", text=text.name)
                op.script = text.name
                op.is_global_script = False

    layout.separator()
    layout.label(text="Global Scripts", icon='FILE_SCRIPT')
    layout.separator()

    global_scripts_path = bpy.context.preferences.addons[__package__].preferences.global_scripts_path

    if os.path.isdir(global_scripts_path):
        for file_name in os.listdir(global_scripts_path):
            if file_name.endswith('.py'):
                display_name = os.path.splitext(file_name)[0]
                op = layout.operator("lk.script_runner_run_script", text=display_name)
                op.script = file_name
                op.is_global_script = True


class LK_SCRIPT_RUNNER_OT_run_script(bpy.types.Operator):
    """Run a selected script from Text Editor"""
    bl_idname = "lk.script_runner_run_script"
    bl_label = "Run Script"
    bl_description = "Run a script from Text Editor"
    bl_options = {'REGISTER'}

    script: bpy.props.StringProperty(default="")
    is_global_script: bpy.props.BoolProperty(default=False)

    def invoke(self, context, event):
        if not self.script:
            bpy.context.window_manager.popup_menu(scripts_menu, title="Script Runner", icon='TEXT')
            return {'CANCELLED'}
        else:
            return self.execute(context)

    def execute(self, context):
        if not self.is_global_script:
            # Run the script from Blender's text datablock
            script = bpy.data.texts.get(self.script)
            if script:
                exec(script.as_string())  # pylint: disable=exec-used
            else:
                self.report({'ERROR'}, f"No datablock named {self.script} found.")
        else:
            # Get the full path to the script file
            global_scripts_path = bpy.context.preferences.addons[__package__].preferences.global_scripts_path
            full_script_path = os.path.join(global_scripts_path, self.script)

            # Run the script from a file
            try:
                with open(full_script_path, 'r', encoding='utf-8') as file:
                    script_content = file.read()
                exec(script_content)  # pylint: disable=exec-used
            except FileNotFoundError:
                self.report({'ERROR'}, f"No file named {self.script} found.")

        self.script = ""
        return {'FINISHED'}


class LKScriptRunnerPreferences(bpy.types.AddonPreferences):
    """Preferences for LK Script Runner"""
    bl_idname = __package__

    global_scripts_path: bpy.props.StringProperty(name="Global Scripts Path", subtype='DIR_PATH', default="", description="Python scripts present in this folder will be available in any Blender file")

    def draw(self, _context):
        layout = self.layout
        layout.label(text="Shortcut:")

        keyconfig_user = bpy.context.window_manager.keyconfigs.user
        window_keymap = keyconfig_user.keymaps.get('Window')

        if window_keymap:
            keymap_item = window_keymap.keymap_items.get("lk.script_runner_run_script")
            if keymap_item:
                rna_keymap_ui.draw_kmi([], keyconfig_user, window_keymap, keymap_item, layout, 0)

        global_scripts_box = layout.box()
        global_scripts_box.prop(self, "global_scripts_path")
        global_scripts_box.label(text="WARNING: Scripts in this folder will be executed without any safety checks. Do not put any scripts you do not 100% trust in this folder.", icon='ERROR')


classes = (
    LK_SCRIPT_RUNNER_OT_run_script,
    LKScriptRunnerPreferences
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    keymaps = bpy.context.window_manager.keyconfigs.user.keymaps
    if keymaps:
        window_keymap = keymaps['Window']
        if window_keymap:
            window_keymap.keymap_items.new(idname="lk.script_runner_run_script", type='R', value='PRESS', ctrl=True)


def unregister():
    window_keymap = bpy.context.window_manager.keyconfigs.user.keymaps['Window']

    if window_keymap:
        keymap_item = window_keymap.keymap_items.get("lk.script_runner_run_script")
        if keymap_item:
            window_keymap.keymap_items.remove(keymap_item)

    for class_to_unregister in reversed(classes):
        bpy.utils.unregister_class(class_to_unregister)


if __name__ == "__main__":
    register()
