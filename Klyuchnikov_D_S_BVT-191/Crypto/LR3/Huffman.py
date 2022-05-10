import wx

class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='Huffman', size=(500,400))
        panel = wx.Panel(self)        
        my_sizer = wx.BoxSizer(wx.VERTICAL)        
        self.text_ctrl = wx.TextCtrl(panel, pos=(20,20))
        self.data = wx.TextCtrl(panel, wx.ID_ANY, size=(400,300),style = wx.TE_MULTILINE|wx.TE_READONLY|wx.VSCROLL)
        my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)   
        my_sizer.Add(self.data, 0, wx.ALL | wx.EXPAND, 5)        
        my_btn = wx.Button(panel, label='Code', pos=(100, 100))
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)        
        panel.SetSizer(my_sizer)       
        self.Show()

    def on_press(self, event):
        message = self.text_ctrl.GetValue()
        self.data.Clear()
        freq = {}
        for c in message:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1

        freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        nodes = freq

        while len(nodes) > 1:
            (key1, c1) = nodes[-1]
            (key2, c2) = nodes[-2]
            nodes = nodes[:-2]
            node = NodeTree(key1, key2)
            nodes.append((node, c1 + c2))

        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
        
        if not message:
            self.data.AppendText("You didn't enter anything!")
        else:
            huffmanCode = huffman_code_tree(nodes[0][0])
            self.data.AppendText('Char | Huffman code\n----------------------\n')
            for (char, frequency) in freq:
                self.data.AppendText(' %-4r |%12s' % (char, huffmanCode[char])+ '\n')

class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()