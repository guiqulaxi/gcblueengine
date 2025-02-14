/** 
**  @file tcStringTable.h
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

#ifndef _STRINGTABLE_H_
#define _STRINGTABLE_H_

#ifdef WIN32
#pragma once
#endif

#include "tcStringArray.h"
#include <string>
#include <vector>

/**
*
*/
namespace scriptinterface 
{
	/**
	* Class for array of stringarrays to pass to python
	*/
	class tcStringTable
	{
	public:
		std::vector<tcStringArray> stringTable;

		void AddStringArray(const tcStringArray& s);
        void PushBack(const tcStringArray& s);
		tcStringArray GetStringArray(unsigned n) const;
		std::string GetString(unsigned n) const;
		unsigned int Size();

        void Clear();
        tcStringTable(const std::vector<std::vector<std::string>> & other) {

            for (int  i= 0; i < other.size(); ++i) {
                tcStringArray sa;
                for (int j = 0; j < other[i].size(); ++j) {
                    sa.PushBack(other[i][j]);
                }
                this->PushBack(sa);
            }

        }
		tcStringTable();
		~tcStringTable();
	};

}

#endif

