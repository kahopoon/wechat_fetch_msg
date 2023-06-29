import requests, uiautomation
import tkinter, tkinter.messagebox

##########################################################################
WECHAT_APP_INSTANCE_NAME = "WeChat" ## Change for languages settings
WECHAT_CONVERSIONS_LIST_NAME = "会话"
WECHAT_CHAT_HISTORY_LIST_NMAE = "消息"

MSG_NO_UNREAD_MSG = "No unread message."
MSG_FETCH_ERROR = "Error in getting unread message."

APP_UNREAD_BTN_NAME = "Get Unread Message Here"
APP_MESSAGE_BOX_TITLE = "Unread Message"

##########################################################################
def getUnreadMsg():
	wechat = uiautomation.WindowControl(Name=WECHAT_APP_INSTANCE_NAME)
	conversations = wechat.ListControl(Name=WECHAT_CONVERSIONS_LIST_NAME)
	unread = conversations.TextControl(searchDepth=4)
	try:
		if unread.Name: # Name = 1 if unread
			unread.Click(simulateMove=False)
			chat_name = unread.GetParentControl().GetChildren()[0].Name # Return chat group name or individual name
			last_msg = wechat.ListControl(Name=WECHAT_CHAT_HISTORY_LIST_NMAE).GetChildren()[-1].Name
			return f"{chat_name}: {last_msg}"
		else:
			return MSG_NO_UNREAD_MSG
	except:
		return MSG_FETCH_ERROR

def showUnreadMsg():
	tkinter.messagebox.showinfo(APP_MESSAGE_BOX_TITLE, getUnreadMsg())

##########################################################################
def main():
    app = tkinter.Tk()
    button = tkinter.Button(app, text=APP_UNREAD_BTN_NAME, command=showUnreadMsg)
    button.pack()
    app.mainloop()

if __name__ == "__main__":
    main()
