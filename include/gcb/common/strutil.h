/**
 ******************************************************************************
 *
 *  @mainpage strutil v1.0.2 - header-only string utility library documentation
 *  @see https://github.com/Shot511/strutil
 *
 *  @copyright  Copyright (C) 2024 Tomasz Galaj
 *  @file       strutil.h
 *  @brief      Library public interface header
 *
 *  @subsection Thank you all for your contributions!!
 *
 ******************************************************************************
 */

#pragma once

#include <algorithm>
#include <cctype>
#include <map>
#include <regex>
#include <sstream>
#include <string>
#include <vector>
#include <array>
#define MAX_STR_LEN 1024
//! The strutil namespace
namespace strutil
{
/**
     * @brief Converts any datatype into std::string.
     *        Datatype must support << operator.
     * @tparam T
     * @param value - will be converted into std::string.
     * @return Converted value as std::string.
     */
template<typename T>
static inline std::string to_string(T value)
{
    std::stringstream ss;
    ss << value;

    return ss.str();
}

/**
     * @brief Converts std::string into any datatype.
     *        Datatype must support << operator.
     * @tparam T
     * @param str - std::string that will be converted into datatype T.
     * @return Variable of datatype T.
     */
template<typename T>
static inline T parse_string(const std::string & str)
{
    T result;
    std::istringstream(str) >> result;

    return result;
}

/**
     * @brief Converts std::string to lower case.
     * @param str - std::string that needs to be converted.
     * @return Lower case input std::string.
     */
static inline std::string to_lower(const std::string & str)
{
    auto result = str;
    std::transform(result.begin(), result.end(), result.begin(), [](unsigned char c) -> unsigned char
    {
        return static_cast<unsigned char>(std::tolower(c));
    });

    return result;
}

/**
     * @brief Converts std::string to upper case.
     * @param str - std::string that needs to be converted.
     * @return Upper case input std::string.
     */
static inline std::string to_upper(const std::string & str)
{
    auto result = str;
    std::transform(result.begin(), result.end(), result.begin(), [](unsigned char c) -> unsigned char
    {
        return static_cast<unsigned char>(std::toupper(c));
    });

    return result;
}

/**
     * @brief Converts the first character of a string to uppercase letter and lowercases all other characters, if any.
     * @param str - input string to be capitalized.
     * @return A string with the first letter capitalized and all other characters lowercased. It doesn't modify the input string.
     */
static inline std::string capitalize(const std::string & str)
{
    auto result = str;
    if (!result.empty())
    {
        result.front() = static_cast<char>(std::toupper(result.front()));
    }

    return result;
}

/**
     * @brief Converts only the first character of a string to uppercase letter, all other characters stay unchanged.
     * @param str - input string to be modified.
     * @return A string with the first letter capitalized. All other characters stay unchanged. It doesn't modify the input string.
     */
static inline std::string capitalize_first_char(const std::string & str)
{
    auto result = to_lower(str);
    if (!result.empty())
    {
        result.front() = static_cast<char>(std::toupper(result.front()));
    }

    return result;
}

/**
     * @brief Checks if input std::string str contains specified substring.
     * @param str - std::string to be checked.
     * @param substring - searched substring.
     * @return True if substring was found in str, false otherwise.
     */
static inline bool contains(const std::string & str, const std::string & substring)
{
    return str.find(substring) != std::string::npos;
}

/**
     * @brief Checks if input std::string str contains specified character.
     * @param str - std::string to be checked.
     * @param character - searched character.
     * @return True if character was found in str, false otherwise.
     */
static inline bool contains(const std::string & str, const char character)
{
    return contains(str, std::string(1, character));
}

/**
     * @brief Compares two std::strings ignoring their case (lower/upper).
     * @param str1 - std::string to compare
     * @param str2 - std::string to compare
     * @return True if str1 and str2 are equal, false otherwise.
     */
static inline bool compare_ignore_case(const std::string & str1, const std::string & str2)
{
    return to_lower(str1) == to_lower(str2);
}

/**
     * @brief Trims (in-place) white spaces from the left side of std::string.
     *        Taken from: http://stackoverflow.com/questions/216823/whats-the-best-way-to-trim-stdstring.
     * @param str - input std::string to remove white spaces from.
     */
static inline void trim_left(std::string & str)
{
    str.erase(str.begin(), std::find_if(str.begin(), str.end(), [](int ch) { return !std::isspace(ch); }));
}

/**
     * @brief Trims (in-place) white spaces from the right side of std::string.
     *        Taken from: http://stackoverflow.com/questions/216823/whats-the-best-way-to-trim-stdstring.
     * @param str - input std::string to remove white spaces from.
     */
static inline void trim_right(std::string & str)
{
    str.erase(std::find_if(str.rbegin(), str.rend(), [](int ch) { return !std::isspace(ch); }).base(), str.end());
}

/**
     * @brief Trims (in-place) white spaces from the both sides of std::string.
     *        Taken from: http://stackoverflow.com/questions/216823/whats-the-best-way-to-trim-stdstring.
     * @param str - input std::string to remove white spaces from.
     */
static inline void trim(std::string & str)
{
    trim_left(str);
    trim_right(str);
}

/**
      * @brief Trims white spaces from the left side of std::string.
      *        Taken from: http://stackoverflow.com/questions/216823/whats-the-best-way-to-trim-stdstring.
      * @param str - input std::string to remove white spaces from.
      * @return Copy of input str with trimmed white spaces.
      */
static inline std::string trim_left_copy(std::string str)
{
    trim_left(str);
    return str;
}

/**
      * @brief Trims white spaces from the right side of std::string.
      *        Taken from: http://stackoverflow.com/questions/216823/whats-the-best-way-to-trim-stdstring.
      * @param str - input std::string to remove white spaces from.
      * @return Copy of input str with trimmed white spaces.
      */
static inline std::string trim_right_copy(std::string str)
{
    trim_right(str);
    return str;
}

/**
      * @brief Trims white spaces from the both sides of std::string.
      *        Taken from: http://stackoverflow.com/questions/216823/whats-the-best-way-to-trim-stdstring.
      * @param str - input std::string to remove white spaces from.
      * @return Copy of input str with trimmed white spaces.
      */
static inline std::string trim_copy(std::string str)
{
    trim(str);
    return str;
}

/**
     * @brief Replaces (in-place) the first occurrence of target with replacement.
     *        Taken from: http://stackoverflow.com/questions/3418231/c-replace-part-of-a-string-with-another-string.
     * @param str - input std::string that will be modified.
     * @param target - substring that will be replaced with replacement.
     * @param replacement - substring that will replace target.
     * @return True if replacement was successfull, false otherwise.
     */
static inline bool replace_first(std::string & str, const std::string & target, const std::string & replacement)
{
    const size_t start_pos = str.find(target);
    if (start_pos == std::string::npos)
    {
        return false;
    }

    str.replace(start_pos, target.length(), replacement);
    return true;
}

/**
     * @brief Replaces (in-place) last occurrence of target with replacement.
     *        Taken from: http://stackoverflow.com/questions/3418231/c-replace-part-of-a-string-with-another-string.
     * @param str - input std::string that will be modified.
     * @param target - substring that will be replaced with replacement.
     * @param replacement - substring that will replace target.
     * @return True if replacement was successfull, false otherwise.
     */
static inline bool replace_last(std::string & str, const std::string & target, const std::string & replacement)
{
    size_t start_pos = str.rfind(target);
    if (start_pos == std::string::npos)
    {
        return false;
    }

    str.replace(start_pos, target.length(), replacement);
    return true;
}

/**
     * @brief Replaces (in-place) all occurrences of target with replacement.
     *        Taken from: http://stackoverflow.com/questions/3418231/c-replace-part-of-a-string-with-another-string.
     * @param str - input std::string that will be modified.
     * @param target - substring that will be replaced with replacement.
     * @param replacement - substring that will replace target.
     * @return >0 if replacement was successfull, 0 otherwise.
     */
static inline size_t replace_all(std::string & str, const std::string & target, const std::string & replacement)
{
    if (target.empty())
    {
        return false;
    }
    size_t count=0;
    size_t start_pos = 0;
    const bool found_substring = str.find(target, start_pos) != std::string::npos;

    while ((start_pos = str.find(target, start_pos)) != std::string::npos)
    {
        str.replace(start_pos, target.length(), replacement);
        start_pos += replacement.length();
        count++;
    }

    return found_substring;
}

/**
     * @brief Checks if std::string str ends with specified suffix.
     * @param str - input std::string that will be checked.
     * @param suffix - searched suffix in str.
     * @return True if suffix was found, false otherwise.
     */
static inline bool ends_with(const std::string & str, const std::string & suffix)
{
    const auto suffix_start = str.size() - suffix.size();
    const auto result = str.find(suffix, suffix_start);
    return (result == suffix_start) && (result != std::string::npos);
}

/**
     * @brief Checks if std::string str ends with specified character.
     * @param str - input std::string that will be checked.
     * @param suffix - searched character in str.
     * @return True if ends with character, false otherwise.
     */
static inline bool ends_with(const std::string & str, const char suffix)
{
    return !str.empty() && (str.back() == suffix);
}

/**
     * @brief Checks if std::string str starts with specified prefix.
     * @param str - input std::string that will be checked.
     * @param prefix - searched prefix in str.
     * @return True if prefix was found, false otherwise.
     */
static inline bool starts_with(const std::string & str, const std::string & prefix)
{
    return str.rfind(prefix, 0) == 0;
}

/**
     * @brief Checks if std::string str starts with specified character.
     * @param str - input std::string that will be checked.
     * @param prefix - searched character in str.
     * @return True if starts with character, false otherwise.
     */
static inline bool starts_with(const std::string & str, const char prefix)
{
    return !str.empty() && (str.front() == prefix);
}

/**
     * @brief Splits input std::string str according to input delim.
     * @param str - std::string that will be splitted.
     * @param delim - the delimiter.
     * @return std::vector<std::string> that contains all splitted tokens.
     */
static inline std::vector<std::string> split(const std::string & str, const char delim)
{
    std::vector<std::string> tokens;
    std::stringstream ss(str);

    std::string token;
    while(std::getline(ss, token, delim))
    {
        tokens.push_back(token);
    }

    // Match semantics of split(str,str)
    if (str.empty() || ends_with(str, delim)) {
        tokens.emplace_back();
    }

    return tokens;
}

/**
     * @brief Splits input std::string str according to input std::string delim.
     *        Taken from: https://stackoverflow.com/a/46931770/1892346.
     * @param str - std::string that will be split.
     * @param delim - the delimiter.
     * @return std::vector<std::string> that contains all splitted tokens.
     */
static inline std::vector<std::string> split(const std::string & str, const std::string & delim)
{
    size_t pos_start = 0, pos_end, delim_len = delim.length();
    std::string token;
    std::vector<std::string> tokens;

    while ((pos_end = str.find(delim, pos_start)) != std::string::npos)
    {
        token = str.substr(pos_start, pos_end - pos_start);
        pos_start = pos_end + delim_len;
        tokens.push_back(token);
    }

    tokens.push_back(str.substr(pos_start));
    return tokens;
}

/**
     * @brief Splits input string using regex as a delimiter.
     * @param src - std::string that will be split.
     * @param rgx_str - the set of delimiter characters.
     * @return vector of resulting tokens.
     */
static inline std::vector<std::string> regex_split(const std::string& src, const std::string& rgx_str)
{
    std::vector<std::string> elems;
    const std::regex rgx(rgx_str);
    std::sregex_token_iterator iter(src.begin(), src.end(), rgx, -1);
    std::sregex_token_iterator end;
    while (iter != end)
    {
        elems.push_back(*iter);
        ++iter;
    }
    return elems;
}

/**
     * @brief Splits input string using regex as a delimiter.
     * @param src - std::string that will be split.
     * @param dest - map of matched delimiter and those being splitted.
     * @param rgx_str - the set of delimiter characters.
     * @return True if the parsing is successfully done.
     */
static inline std::map<std::string, std::string> regex_split_map(const std::string& src, const std::string& rgx_str)
{
    std::map<std::string, std::string> dest;
    std::string tstr = src + " ";
    std::regex rgx(rgx_str);
    std::sregex_token_iterator niter(tstr.begin(), tstr.end(), rgx);
    std::sregex_token_iterator viter(tstr.begin(), tstr.end(), rgx, -1);
    std::sregex_token_iterator end;
    ++viter;
    while (niter != end)
    {
        dest[*niter] = *viter;
        ++niter;
        ++viter;
    }

    return dest;
}

/**
     * @brief Splits input string using any delimiter in the given set.
     * @param str - std::string that will be split.
     * @param delims - the set of delimiter characters.
     * @return vector of resulting tokens.
     */
static inline std::vector<std::string> split_any(const std::string & str, const std::string & delims)
{
    std::string token;
    std::vector<std::string> tokens;

    size_t pos_start = 0;
    for (size_t pos_end = 0; pos_end < str.length(); ++pos_end)
    {
        if (contains(delims, str[pos_end]))
        {
            token = str.substr(pos_start, pos_end - pos_start);
            tokens.push_back(token);
            pos_start = pos_end + 1;
        }
    }

    tokens.push_back(str.substr(pos_start));
    return tokens;
}

/**
     * @brief Joins all elements of std::vector tokens of arbitrary datatypes
     *        into one std::string with delimiter delim.
     * @tparam T - arbitrary datatype.
     * @param tokens - vector of tokens.
     * @param delim - the delimiter.
     * @return std::string with joined elements of vector tokens with delimiter delim.
     */
template<typename T>
static inline std::string join(const std::vector<T> & tokens, const std::string & delim)
{
    std::ostringstream result;
    for(auto it = tokens.begin(); it != tokens.end(); ++it)
    {
        if(it != tokens.begin())
        {
            result << delim;
        }

        result << *it;
    }

    return result.str();
}

/**
     * @brief Inplace removal of all empty strings in a vector<string>
     * @param tokens - vector of strings.
     */
static inline void drop_empty(std::vector<std::string> & tokens)
{
    auto last = std::remove_if(tokens.begin(), tokens.end(), [](const std::string& s){ return s.empty(); });
    tokens.erase(last, tokens.end());
}

/**
     * @brief Inplace removal of all empty strings in a vector<string>
     * @param tokens - vector of strings.
     * @return vector of non-empty tokens.
     */
static inline std::vector<std::string> drop_empty_copy(std::vector<std::string> tokens)
{
    drop_empty(tokens);
    return tokens;
}

/**
     * @brief Creates new std::string with repeated n times substring str.
     * @param str - substring that needs to be repeated.
     * @param n - number of iterations.
     * @return std::string with repeated substring str.
     */
static inline std::string repeat(const std::string & str, unsigned n)
{
    std::string result;

    for(unsigned i = 0; i < n; ++i)
    {
        result += str;
    }

    return result;
}

/**
     * @brief Creates new std::string with repeated n times char c.
     * @param c - char that needs to be repeated.
     * @param n - number of iterations.
     * @return std::string with repeated char c.
     */
static inline std::string repeat(char c, unsigned n)
{
    return std::string(n, c);
}

/**
     * @brief Checks if input std::string str matches specified reular expression regex.
     * @param str - std::string to be checked.
     * @param regex - the std::regex regular expression.
     * @return True if regex matches str, false otherwise.
     */
static inline bool matches(const std::string & str, const std::regex & regex)
{
    return std::regex_match(str, regex);
}


/**
     * @brief Reverse input std::vector<std::string> strs.
     * @param strs - std::vector<std::string> to be checked.
     */
template<typename T>
static inline void reverse_inplace(std::vector<T> &strs)
{
    std::reverse(strs.begin(), strs.end());
}

/**
     * @brief Reverse input std::vector<std::string> strs.
     * @param strs - std::vector<std::string> to be checked.
     */
template<typename T>
static inline std::vector<T> reverse_copy(std::vector<T> strs)
{
    std::reverse(strs.begin(), strs.end());
    return strs;
}
template <typename... Args>
static inline std::string format(const std::string & foramtstr,Args ...args)
{

    // 预估输出字符串的大小，这只是一个粗略的估计，可能需要调整
    //            size_t size = std::strlen(formatstr) * sizeof...(args) + 1;
    char buffer[MAX_STR_LEN];

    // 使用sprintf将格式化的字符串写入到buffer中
    int result = sprintf(buffer, foramtstr.c_str(), args...);

    // 如果sprintf返回的结果大于或等于预估的大小，说明发生了缓冲区溢出
    if (result >= MAX_STR_LEN) {
        // 这里可以抛出一个异常或者采取其他错误处理措施
        throw std::runtime_error("Buffer overflow in format function");
    }
    // 使用string构造函数将C风格字符串转换为std::string
    std::string formatted(buffer, result);
    return formatted;
}
/**
     * @brief 通配符匹配 *代替零个、单个或多个字符 ?代表单个字符
     * @param str
     * @param pattern
     */
static bool wildcard_match(const std::string& s, const std::string& p)
{
    const int m = p.length();
    const int n = s.length();
    std::vector<std::vector<bool>> dp(m + 1, std::vector<bool>(n + 1));
    dp[0][0] = true;
    for (int i = 0; (i < m)&&('*'==p[i]); i++)
    {
        dp[i + 1][0] = true;//p前面的*不匹配任何字符
    }
    for (int i = 1; i <= m; i++)
    {
        const char& ch = p[i - 1];
        for (int j = 1; j <= n; j++)
        {
            if ('*' == ch)
            {
                const bool b1 = dp[i - 1][j];//*不匹配任何字符
                const bool b2 = dp[i][j - 1];//*匹配字符1到x个字符
                dp[i][j] = b1 || b2;
            }
            else if ('?' == ch)
            {
                dp[i][j] =  dp[i - 1][j - 1];
            }
            else
            {
                dp[i][j] = dp[i - 1][j - 1]&&(ch == s[j-1]);
            }
        }
    }
    return dp.back().back();
}

static std::string to_python_value(const std::vector<int>& data)
{
    std::string valueString;
    valueString+= "[";
    for (size_t i = 0; i < data.size(); ++i) {
        valueString += std::to_string(data[i]);
        if (i < data.size() - 1) {
            valueString += ",";
        }
    }
    valueString+= "]";
    return valueString;
}
static std::string to_python_value(const std::vector<unsigned short>& data)
{
    std::string valueString;
    valueString+= "[";
    for (size_t i = 0; i < data.size(); ++i) {
        valueString += std::to_string(data[i]);
        if (i < data.size() - 1) {
            valueString += ",";
        }
    }
    valueString+= "]";
    return valueString;
}

static std::string to_python_value(const std::vector<unsigned int>& data)
{
    std::string valueString;
    valueString+= "[";
    for (size_t i = 0; i < data.size(); ++i) {
        valueString += std::to_string(data[i]);
        if (i < data.size() - 1) {
            valueString += ",";
        }
    }
    valueString+= "]";
    return valueString;
}
static std::string to_python_value(const std::vector<float>&  data)
{
    std::string valueString;
    valueString+= "[";
    for (size_t i = 0; i < data.size(); ++i) {
        valueString += std::to_string(data[i]);
        if (i < data.size() - 1) {
            valueString += ",";
        }
    }
    valueString+= "]";
    return valueString;
}
static std::string to_python_value(const std::vector<std::string>& data)
{
     std::string valueString;
    valueString+= "[";
    for (size_t i = 0; i < data.size(); ++i) {
        valueString += "'";
        valueString += data[i];
        valueString += "'";
        if (i < data.size() - 1) {
            valueString += ",";
        }
    }
    valueString+= "]";
    return valueString;
}
static std::string to_python_value(const std::vector<bool>& data)
{
    std::string valueString;
    valueString+= "[";
    for (size_t i = 0; i < data.size(); ++i) {
        valueString += data[i]?"True":"False";
        if (i < data.size() - 1) {
            valueString += ",";
        }
    }
    valueString+= "]";
    return valueString;
}
static std::string to_python_value(const std::string& data)
{
    std::string valueString;

    valueString += "'"+data+"'";

    return valueString;
}
static std::string to_python_value(const char* data)
{
    std::string valueString;

    valueString += "'"+std::string(data)+"'";

    return valueString;
}
static std::string to_python_value(bool data)
{
    std::string valueString;
    valueString += data?"True":"False";

    return valueString;
}
static std::string to_python_value(int data)
{
    std::string valueString;
    valueString += std::to_string(data);

    return valueString;
}
static std::string to_python_value(float data)
{
    std::string valueString;
    valueString +=std::to_string(data);

    return valueString;
}
static std::string to_python_value(double data)
{
    std::string valueString;
    valueString +=std::to_string(data);

    return valueString;
}
static std::string to_python_value(long data)
{
    std::string valueString;
    valueString += std::to_string(data);

    return valueString;
}
static std::string to_python_value(unsigned long data)
{
    std::string valueString;
    valueString += std::to_string(data);

    return valueString;
}
static std::string to_python_value(unsigned int data)
{
    std::string valueString;
    valueString += std::to_string(data);

    return valueString;
}
}
