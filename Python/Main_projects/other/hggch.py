from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.recycleview.views import RecycleDataViewBehavior


class MyButton(RecycleDataViewBehavior, ToggleButton):
    index = None

    def refresh_view_attrs(self, rv, index, data):
        """ Catch and handle the view changes """
        self.index = index
        return super(MyButton, self).refresh_view_attrs(
            rv, index, data)


class TestRecycleView(RecycleView):
    items_per_row = 3
    selected_data = None
    selected_row = None

    def find_row(self, instance):
        rgl = self.ids.gl
        num_buttons = len(rgl.children)
        num_rows = num_buttons // self.items_per_row
        self.selected_row = instance.index // self.items_per_row + 1
        print('Row: ', self.selected_row)
        self.selected_data = self.data[(self.selected_row - 1) * self.items_per_row: self.items_per_row
                                                                                     * self.selected_row]
        print('Data: ', self.selected_data)
        index1 = (num_rows - self.selected_row + 1) * self.items_per_row - 1
        index2 = index1 - self.items_per_row
        state = instance.state
        for index in range(index1, index2, -1):
            rgl.children[index].state = state

        print('======================')
        print('    Add some data     ')
        print('======================')

        # See how index[0] changes between the refresh()
        rgl.children[0].state = "down"
        root = App.get_running_app().root
        root.refresh_from_data()


KV = '''

<MyButton>:
    on_release:
        app.root.find_row(self)

TestRecycleView:
    data: [{'text': str(x)} if x not in range(9,12) else {'text': 'Press here'} for x in range(21)]
    viewclass: 'MyButton'
    id: rv_controller
    target_id: None
    RecycleGridLayout:
        id: gl
        cols: 3
        default_size_hint: 1, None
        orientation: 'vertical'
        key_selection: 'selectable'
        default_size: None, dp(26)
        size_hint_y: None
        height: self.minimum_height
        multiselect: True
        touch_multiselect: True

'''


class Test(App):
    def build(self):
        root = Builder.load_string(KV)
        # root.data = items
        return root


Test().run()
