/**
** @file tcDateTime.cpp
*/
/*
**  Copyright (c) 2014, GCBLUE PROJECT
**  All rights reserved.
**
**  Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
**
**  1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
**
**  2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the 
**     documentation and/or other materials provided with the distribution.
**
**  3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from 
**     this software without specific prior written permission.
**
**  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT 
**  NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE 
**  COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES 
**  (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) 
**  HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING 
**  IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

#ifdef WX_PRECOMP
//#include "stdwx.h"
#else
////#include "wx/wx.h" 
#endif

#include "tcDateTime.h"
#include <chrono>
#include "common/tcStream.h"
//#include "wx/datetime.h"
#include <cmath>
#include <cassert>
#include "strutil.h"
#ifdef _DEBUG
#define new DEBUG_NEW
#endif


const int tcDateTime::yearOrdinal[13] = {0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334};


/**
* @return true if time is earlier than rhs
*/
bool tcDateTime::operator<(const tcDateTime& rhs) const
{
    return (GetTimeT() < rhs.GetTimeT());
}

/**
* @return true if time is later than rhs
*/
bool tcDateTime::operator>(const tcDateTime& rhs) const
{
    return (GetTimeT() > rhs.GetTimeT());
}


/**
* Loads state from stream
*/
tcStream& tcDateTime::operator<<(tcStream& stream)
{
    uint64_t total_millis;
    stream>>total_millis;
    time_p = std::chrono::system_clock::from_time_t(0); + std::chrono::milliseconds(total_millis);

    return stream;
}

/**
* Saves state to stream
*/
tcStream& tcDateTime::operator>>(tcStream& stream)
{
    auto duration_since_epoch = std::chrono::duration_cast<std::chrono::milliseconds>(
           time_p-std::chrono::system_clock::from_time_t(0)
       );
   uint64_t cn= duration_since_epoch.count();
   stream<<cn;
//    stream << year;
//    stream << month;
//    stream << day;
//    stream << hour;

    return stream;
}
void tcDateTime::AdjustTimeMilliseconds(uint64_t dt_ms)
{
    std::chrono::milliseconds ms(dt_ms);
    time_p+=ms;
}

void tcDateTime::AdjustTimeHours(double dt_hr)
{
      AdjustTimeMilliseconds((uint64_t)(dt_hr*3600000));
//    double floor_current_hour = std::floor(hour);
//    int int_current_hour = int(floor_current_hour);
//    double fract_current_hour = hour - floor_current_hour;

//    std::chrono::system_clock::time_point current(GetJulianDate());
//    //const std::chrono::system_clock::time_point current(day, const std::chrono::system_clock::time_point::Month(month-1), year, int_current_hour, 0, 0, 0);
//    //current.MakeUTC();

//    double floor_dt_hr = std::floor(dt_hr);
//    double fract_dt_hr = dt_hr - floor_dt_hr; // fractional part of dt_hr

//    int int_dt_hr = int(floor_dt_hr);
//    wxTimeSpan span(int_dt_hr, 0, 0, 0);
//    //span.Set(int(floor_dt_hr));

//    current = current.Add(span);

//    year = current.GetYear(const std::chrono::system_clock::time_point::GMT0);
//    month = int(current.GetMonth(const std::chrono::system_clock::time_point::GMT0)) + 1;
//    day = current.GetDay(const std::chrono::system_clock::time_point::GMT0);
//    hour = double(current.GetHour(const std::chrono::system_clock::time_point::GMT0)) + fract_current_hour;

//    AdjustTimeSeconds(3600.0 * fract_dt_hr);
}

uint64_t tcDateTime::GetTimeT() const
{
    auto epoch = std::chrono::system_clock::from_time_t(0);
            // 计算两个时间点之间的duration
    auto duration = time_p - epoch;
            // 将duration转换为毫秒
    auto millis = std::chrono::duration_cast<std::chrono::milliseconds>(duration).count();
    return millis;
}

/**
* Use this for small time adjustments, less than 24 hours
*/
void tcDateTime::AdjustTimeSeconds(double dt_s)
{
   AdjustTimeMilliseconds((uint64_t)(dt_s*1000));
//    double dt_hr = 0.000277777777777778 * dt_s; // hours

//    assert(fabsf(dt_hr) < 24.0);

//    hour += dt_hr;

//    // update for rollover
//    if ((hour >= 0) && (hour < 24.0))
//    {
//        return;
//    }
//    else if (hour >= 24.0)
//    {
//        hour -= 24.0;
//        day++;
//        if (day > LastDayInMonth())
//        {
//            month++;
//            day = 1;
//            if (month > 12)
//            {
//                year++;
//                month = 1;
//            }
//        }
//    }
//    else if (hour < 0)
//    {
//        hour += 24.0;
//        day--;
//        if (day < 1)
//        {
//            month--;
//            if (month < 1)
//            {
//                month = 12;
//                year--;
//            }
//            day = LastDayInMonth();
//        }
//    }

}

const char* tcDateTime::asString() const
{
    static std::string s;

    s=strutil::format("%04d/%02d/%02d %02d%02d%02d",
        GetYear(), GetMonth(), GetDay(), GetHour(), GetMinute(), GetSecond());

    return s.c_str();
}

/**
* @return time of day string
*/
const char* tcDateTime::asStringTOD() const
{
    static std::string s;

    s=strutil::format("%02d:%02d:%02d",
        GetHour(), GetMinute(), GetSecond());

    return s.c_str();
}

double tcDateTime::GetHoursUTC() const
{
    return  GetHour();
}

int tcDateTime::GetDayOfYear() const
{
     std::chrono::system_clock::from_time_t(0);
    int leapDay = (GetMonth() > 2) && IsLeapYear(GetYear()) ? 1 : 0;

//    int days = yearOrdinal[month];
    return GetDay() + yearOrdinal[GetMonth()] + leapDay;
}

/**
* Formula from http://aa.usno.navy.mil/faq/docs/JD_Formula.html
* JD = 367K - <(7(K+<(M+9)/12>))/4> + <(275M)/9> + I + 1721013.5 + UT/24 - 0.5sign(100K+M-190002.5) + 0.5
* Last 2 terms are skipped assuming a date range of 1900 Mar 1 to 2099 Dec 30
*/
//double tcDateTime::GetJulianDate() const
//{
//    const double inv12 = 1.0 / 12.0;
//    const double inv24 = 1.0 / 24.0;
//    const double r7ov4 = 7.0 / 4.0;
//    const double r275ov9 = 275.0 / 9.0;

//    double fYear = double(year);
//    double fMonth = double(month);
//    double fDay = double(day);

//    double julianDate = 367.0*fYear;
//    julianDate -= floor(r7ov4 * (fYear + floor(inv12 * (fMonth + 9.0))));
//    julianDate += floor(r275ov9 * fMonth) + fDay + 1721013.5 + (inv24 * hour);

//    return julianDate;
//}

/**
* @return float year with fractional value for precise date
* only uses middle of current month for date estimate
*/
float tcDateTime::GetFractionalYear() const
{
    return (float(GetYear()) + (1/12.0f)*(float(GetMonth())-0.5f));
}

int tcDateTime::GetYear() const
{
    std::time_t t = std::chrono::system_clock::to_time_t(time_p);
    std::tm* t_tm = std::localtime(&t);
    return t_tm->tm_year+ 1900;
}

int tcDateTime::GetMonth() const
{
    std::time_t t = std::chrono::system_clock::to_time_t(time_p);
    std::tm* t_tm = std::localtime(&t);
    return t_tm->tm_mon+1;

}

//const char* tcDateTime::GetMonthString() const
//{
//    switch (month)
//    {
//    case 1: return "January"; break;
//    case 2: return "February"; break;
//    case 3: return "March"; break;
//    case 4: return "April"; break;
//    case 5: return "May"; break;
//    case 6: return "June"; break;
//    case 7: return "July"; break;
//    case 8: return "August"; break;
//    case 9: return "September"; break;
//    case 10: return "October"; break;
//    case 11: return "November"; break;
//    case 12: return "December"; break;
//    default: return "Unknown"; break;
//    }
//}

int tcDateTime::GetDay() const
{
    std::time_t t = std::chrono::system_clock::to_time_t(time_p);
    std::tm* t_tm = std::localtime(&t);
    return t_tm->tm_mday;
}

int tcDateTime::GetHour() const
{
    std::time_t t = std::chrono::system_clock::to_time_t(time_p);
    std::tm* t_tm = std::localtime(&t);
    return int(t_tm->tm_hour);
}

int tcDateTime::GetMinute() const
{
    std::time_t t = std::chrono::system_clock::to_time_t(time_p);
    std::tm* t_tm = std::localtime(&t);
    return t_tm->tm_min;

}

int tcDateTime::GetSecond() const
{
    std::time_t t = std::chrono::system_clock::to_time_t(time_p);
    std::tm* t_tm = std::localtime(&t);
    return int(t_tm->tm_sec);
}


bool tcDateTime::IsLeapYear(int y) const
{
    return ((GetYear() % 4) == 0) && (((GetYear() % 100) != 0) || ((GetYear() % 400) == 0));
}

/**
* @return last day in current month
*/
int tcDateTime::LastDayInMonth()
{
    if (GetMonth() != 2)
    {
        return yearOrdinal[GetMonth()] - yearOrdinal[GetMonth()-1];
    }
    else
    {
        int leapDay = (GetMonth() > 2) && IsLeapYear(GetMonth()) ? 1 : 0;
        return 28 + leapDay;
    }
}

tcDateTime::tcDateTime(int year, int month, int day, double hour_utc)
{
    // 创建一个tm结构体来表示本地时间
       std::tm tm_time = {};
       tm_time.tm_year = year - 1900; // tm_year是从1900年开始计数的
       tm_time.tm_mon = month - 1;    // tm_mon是从0开始计数的，即0代表1月
       tm_time.tm_mday = day;
       tm_time.tm_hour = hour_utc;
       tm_time.tm_min = 0;
       tm_time.tm_sec = 0;

       // 将tm结构体转换为time_t表示的自Unix纪元以来的秒数
       time_t time_since_epoch = std::mktime(&tm_time);

       // 返回time_point对象
        time_p=std::chrono::system_clock::from_time_t(time_since_epoch);
}

tcDateTime::tcDateTime(int year, int month, int day, int hour, int min, int sec)
{
    // 创建一个tm结构体来表示本地时间
       std::tm tm_time = {};
       tm_time.tm_year = year - 1900; // tm_year是从1900年开始计数的
       tm_time.tm_mon = month - 1;    // tm_mon是从0开始计数的，即0代表1月
       tm_time.tm_mday = day;
       tm_time.tm_hour = hour;
       tm_time.tm_min = min;
       tm_time.tm_sec = sec;

       // 将tm结构体转换为time_t表示的自Unix纪元以来的秒数
       time_t time_since_epoch = std::mktime(&tm_time);

       // 返回time_point对象
        time_p=std::chrono::system_clock::from_time_t(time_since_epoch) ;
}


tcDateTime::tcDateTime()
{

}

tcDateTime::~tcDateTime() 
{
}

tcDateTime tcDateTime::Now()
{
    tcDateTime dt;
    dt.time_p = std::chrono::system_clock::now();
    return dt;
}
