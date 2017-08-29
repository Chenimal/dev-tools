//
//  APIActionConstants.h
//  lalamove
//
//  Created by Gary Lip on 18/1/2016.
//  Copyright © 2016 Lalamove. All rights reserved.
//

#pragma mark - Data Cache

static NSString *const VAN_META = @"meta2";

static NSString *const VAN_LOOKUP = @"vanlookup";

static NSString *const VAN_SPOT = @"vanspot";

static NSString *const VAN_NORMAL_REQ = @"vannormalrequest";

static NSString *const VAN_SPECIAL_REQ = @"vanspecialrequest";

#pragma mark - User Old Login || Driver Login

static NSString *const VAN_ENROLL = @"vanenroll";

static NSString *const VAN_VERIFY = @"vanverify";

static NSString *const VAN_LOGIN = @"vanlogin";

static NSString *const VAN_LOGOUT = @"vanlogout";

#pragma mark - Driver Registration

static NSString *const VAN_DRIVER_UPLOAD_REGISTER_PHOTO = @"vanuploadlookup";

static NSString *const VAN_REGISTER_FIELD_LOOKUP = @"vanregisterlookup";

static NSString *const VAN_UPLOAD_DRIVER_REG_PHOTO = @"vanupload";

#pragma mark - User Login & Refresh Token

static NSString *const VAN_AUTH_SERVER_USER_LOGIN = @"login";

static NSString *const VAN_API_SERVER_USER_LOGIN = @"vanauthlogin";

static NSString *const VAN_USER_LOGOUT = @"vanauthlogout";

static NSString *const VAN_AUTH_REFRESH_TOKEN = @"vanauthrefreshtoken";

static NSString *const VAN_UPDATE_PROFILE = @"updatePreferences";

static NSString *const VAN_CHANGE_USER_PASSWORD = @"changeUserPassword";

#pragma mark - User Register & SMS Verification

static NSString *const VAN_AUTH_USER_REGISTRATION = @"registration";

static NSString *const VAN_AUTH_USER_REGISTER = @"register";

static NSString *const VAN_RESEND_USER_SMS_VERIFICATION_CODE = @"resendVerificationCode";

static NSString *const VAN_USER_VERIFY_SMS_CODE = @"verifyCode";

static NSString *const VAN_SEND_VERIFICATION_EMAIL = @"resendEmailVerification";

static NSString *const VAN_ADD_PROFILE = @"addProfile";

static NSString *const VAN_USER_CHANGE_LOGIN_PW = @"changeLoginPassword";

static NSString *const VAN_USER_GET_USER_PROFILE = @"getUserProfile";

static NSString *const VAN_AUTH_REQUEST_FOR_RESET_PW = @"getUserEmailOrMobile";

static NSString *const VAN_AUTH_FORGET_PW_SMS_VERIFY = @"GetPendingSMSUserByUUID";

static NSString *const VAN_AUTH_USER_RESET_PW = @"setNewPasswordBySMSAndUUID";

#pragma mark - Price Calculation & Place Order

static NSString *const VAN_PRICECAL = @"vanpricecal";

static NSString *const VAN_REQUEST = @"vanrequest";

#pragma mark - Driver Pickup Order List & Pick Up Order & Set Area Filter Selection

static NSString *const VAN_REQUEST_LIST = @"vanrequestlist";

static NSString *const VAN_REQUEST_DETAIL = @"vanrequestdetail";

static NSString *const VAN_PICKUP_ORDER = @"vaninterest";

static NSString *const VAN_ADDRESS_STR_UPDATE = @"vanaddressstrupdate";

static NSString *const VAN_UPDATE_DRIVER_DUTY = @"vanupdatedriverduty";

#pragma mark - History & Radar Page Info & Add Tips

static NSString *const VAN_SEARCHING_DRIVER_PAGE_INFO = @"vanorderwaiting";

static NSString *const VAN_HISTORY_LIST = @"vanhistorylist";

static NSString *const VAN_HISTORY_DETAIL = @"vanhistory";

static NSString *const VAN_ADD_TIPS = @"vanaddtips";

static NSString *const VAN_SEND_TO_ALL_DRIVER = @"vanfleetorderend";

#pragma mark - Rate and Comment TO User/Driver & Driver Comment List

static NSString *const VAN_COMMENT = @"vancomment";

static NSString *const VAN_RATING = @"vanrating";

static NSString *const VAN_COMMENT_LIST = @"vancommentlist";

#pragma mark - Order Status Change

static NSString *const VAN_COMPLETE = @"vancomplete";

static NSString *const VAN_PICKED_UP_ITEM = @"vanPickup";

static NSString *const VAN_USER_CANCEL = @"vancancel";

static NSString *const VAN_DRIVER_CANCEL = @"vanreject";

#pragma mark - MY_FLEET

static NSString *const VAN_MY_FLEET = @"vanmyfleet";

#pragma mark - Share Order

static NSString *const VAN_SHARE = @"vanshare";

#pragma mark - Wallet of user and driver

static NSString *const VAN_WALLET_BALANCE = @"vanwalletbalance";

static NSString *const VAN_WALLET_AMOUNT = @"vanwalletamount";

static NSString *const VAN_WALLET_RECORDS = @"vanwalletrecords";

static NSString *const VAN_WALLET_HISTORY = @"vanwallethistory";

static NSString *const VAN_DRIVER_PAYMENT_DETAILS = @"vandriverpaymentdetails";

static NSString *const VAN_WALLET_CASHOUT = @"vanwalletcashout";

static NSString *const VAN_WALLET_BANK_INFO = @"vanwalletbankinfo";

#pragma mark - Account info and Update settings

static NSString *const VAN_ACCOUNT = @"vanaccount";

static NSString *const VAN_SET_ACCOUNT_INFO = @"vanaccountinfo"; //included langugae, email, name

static NSString *const VAN_UPDATE_SOUND_ALERT = @"updateSoundAlert";

static NSString *const VAN_ACCOUNT_RATING = @"vanaccountrating"; // driver account rating

#pragma mark - User Locate Driver & Driver update gps location

static NSString *const VAN_LOCATE_DRIVER = @"vanlocatedriver";

static NSString *const VAN_SEND_DRIVER_GPS_LOCATION = @"vanlocation";

#pragma mark - Get News

static NSString *const VAN_NEWS = @"vannotification";

#pragma mark - Get Speical Notification

static NSString *const VAN_SPECIAL_NOTIFICATION = @"vanspecialnotifications";

#pragma mark - Get Welcome News

static NSString *const VAN_WELCOME_INFO = @"vanwelcomeinfo";

#pragma mark - Event Tracker (Check update location frequency for driver)

static NSString *const VAN_EVENT_TRACKER = @"vaneventtracker";

//may be need to use in the future
static NSString *const SEND_TO_ALL_DRIVER = @"publicfavoriteorder";

#pragma mark - Get User Recent Used location info (User who logged in)

static NSString *const VAN_RECENT_LOCAITON = @"vanrecentlocation";

#pragma mark - Special order history status change

static NSString *const UPDATE_ROUTE_STATUS = @"updateroutestatus";

static NSString *const UPDATE_DELIVERY_STATUS = @"updatedeliverystatus";

static NSString *const UPDATE_STOP_STATUS = @"updatestopstatus";

#pragma mark - Special order update purcahse info

static NSString *const UPDATE_PURCHASE_INFO = @"updatepurchaseinfo";

#pragma mark - Special order driver called client

static NSString *const MAKE_CALL = @"makecall";

#pragma mark - Set driver has called user already

static NSString *const VAN_DIAL_BY_DRIVER = @"vandialbydriver";

#pragma mark - Driver geofence tracking

static NSString *const VAN_GEOFENCES = @"vangeofences";

static NSString *const VAN_GEOFENCE_TRANSITION = @"vangeofencetransition";

