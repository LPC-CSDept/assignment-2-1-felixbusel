def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    m_num = int(input('Number of Male Students: '))
    f_num = int(input('Number of Female Students: '))
    total_num = m_num+f_num
    
    m_perc = (m_num/total_num)*100
    f_perc = (f_num/total_num)*100

    print('Total Number of Students: ', total_num)
    print('Males: ', m_num, '\t', 'Females: ', f_num)
    print(f'Percent Male: {m_perc:.2f} % \t Percent Female: {f_perc:.2f} %')
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()