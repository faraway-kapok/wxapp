// pages/weather.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    city: '',
    current: null,
    future: []
  },
  bindKeyInput(e) {
    this.setData({
      city: e.detail.value
    })
  }, 
  query: function(){
    let self = this;
    wx.request({
      url: 'http://192.168.43.39:5000/weather/list?city=' + this.data.city,
      success(res) {
        let data = res.data;
        if (data.errcode != 0) {
          wx.showToast({
            title: data.errmsg,
            icon: 'none',
            duration: 2000
          })
          return;
        }
        self.setData({
          current: data.data.realtime,
          future: data.data.future
        })
        console.log(res.data)
      }
    })
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})