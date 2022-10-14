from mitmproxy import ctx


class ModifyResponse:
    def HackEmbyVerifyRes(self, flow, res):
        flow.response.status_code = 200
        flow.response.headers["content-type"] = "application/json"
        flow.response.set_text(res)
        ctx.log.info('rewrite emby verify url res succ')

    def response(self, flow):
        # 拦截指定的url
        if flow.request.url.startswith("https://mb3admin.com/admin/service/registration/validateDevice"):
            res = '{"cacheExpirationDays":999,"message":"Device Valid","resultCode":"GOOD"}'
            self.HackEmbyVerifyRes(flow, res)
        elif flow.request.url.startswith("https://mb3admin.com/admin/service/registration/validate"):
            res = '{"featId": "","registered": true,"expDate": "2099-01-01","key": ""}'
            self.HackEmbyVerifyRes(flow, res)
        elif flow.request.url.startswith("https://mb3admin.com/admin/service/registration/getStatus"):
            res = '{planType: "Lifetime", deviceStatus: 0, subscriptions: []}'
            self.HackEmbyVerifyRes(flow, res)
        elif flow.request.url.startswith("https://mb3admin.com/admin/service/appstore/register"):
            res = '{"featId": "","registered": true,"expDate": "2099-01-01","key": ""}'
            self.HackEmbyVerifyRes(flow, res)
        elif flow.request.url.startswith("https://mb3admin.com/emby/Plugins/SecurityInfo"):
            res = '{SupporterKey: "", IsMBSupporter: true}'
            self.HackEmbyVerifyRes(flow, res)


addons = [
    ModifyResponse()
]
