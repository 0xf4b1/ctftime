
void main()
{
  char *pcParm1 = "\\PJ\\fC|)L0LTw@Yt@;Twmq0Lw|qw@w2$a@0;w|)@awmLL|Tw|)LwZL2lhhL0k";
  char *__dest;
  int sVar1;
  int local_30;
  
  __dest = (char *)malloc(0x40);
  memset(__dest,0,0x40);
  strcpy(__dest,pcParm1);
  sVar1 = strlen(__dest);
  local_30 = 0;
  while (local_30 < (int)sVar1) {
    __dest[(long)local_30] =
         (char)((int)((((int)__dest[(long)local_30] ^ 0xfU) - 0x1d) * 8) % 0x5f) + ' ';
    local_30 = local_30 + 1;
  }
  puts(__dest);
  return;
}
